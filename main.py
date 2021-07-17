import copy
from random import choice
import pygame
import sys


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (50, 155, 50)
GREY = (180, 180, 180)


def initiate_grid(arr, s):
    for i in range(s):
        arr.append([])
        for j in range(s):
            arr[i].append(0)


def generate(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = choice((1, 0))


def get_neighbours(arr, i, j):
    if i == len(arr) - 1:
        if j == len(arr[0]) - 1:
            return arr[i][j-1], arr[i-1][j-1], arr[i-1][j]
        elif j == 0:
            return arr[i][j+1], arr[i-1][j+1], arr[i-1][j]
        else:
            return arr[i][j+1], arr[i][j-1], arr[i-1][j-1], arr[i-1][j+1], arr[i-1][j]
    elif i == 0:
        if j == len(arr[0]) - 1:
            return arr[i][j-1], arr[i+1][j-1], arr[i+1][j]
        elif j == 0:
            return arr[i][j+1], arr[i+1][j+1], arr[i][j+1]
        else:
            return arr[i][j+1], arr[i][j-1], arr[i+1][j-1], arr[i+1][j+1], arr[i+1][j]
    else:
        if j == len(arr[0]) - 1:
            return arr[i][j-1], arr[i-1][j-1], arr[i-1][j], arr[i+1][j-1], arr[i+1][j]
        elif j == 0:
            return arr[i][j+1], arr[i-1][j+1], arr[i-1][j], arr[i+1][j+1], arr[i+1][j]
        else:
            return arr[i][j+1], arr[i][j-1], arr[i-1][j-1], arr[i-1][j], arr[i-1][j+1], arr[i+1][j-1], arr[i+1][j], arr[i+1][j+1]


def next_generation(arr):
    duplicate = copy.deepcopy(arr)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            neighbours = get_neighbours(arr, i, j)

            if neighbours.count(1) < 2 and arr[i][j] == 1:
                duplicate[i][j] = 0
            elif neighbours.count(1) > 3 and arr[i][j] == 1:
                duplicate[i][j] = 0
            elif neighbours.count(1) == 3 and arr[i][j] == 0:
                duplicate[i][j] = 1
            else:
                pass

    return duplicate


def display(screen, arr):
    size = len(arr)

    side = 450//size

    for i in range(size):
        for j in range(size):
            if arr[i][j] == 1:
                state = 0
            else:
                state = 1

            pygame.draw.rect(screen, BLACK, (75 + i*side, 125 + j*side, side, side), width=state)

    for i in range(size):
        for j in range(size):
            pygame.draw.rect(screen, GREY, (75 + i * side, 125 + j * side, side, side), width=1)

    pygame.display.update()


if __name__ == '__main__':
    pygame.init()

    font = pygame.font.Font("OdibeeSans-Regular.ttf", 25)

    restart_text = txt = font.render("Restart", True, (255, 255, 255))

    win = pygame.display.set_mode((600, 650))
    pygame.display.set_caption("Conway's Game of life")

    universe = []
    n = 30
    initiate_grid(universe,  n)

    generate(universe)

    while True:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 220 <= mouse[0] <= 370 and 30 <= mouse[1] <= 90:
                    universe = []
                    initiate_grid(universe, n)

                    generate(universe)

        win.fill(WHITE)

        pygame.draw.rect(win, (0, 0, 0), pygame.Rect(220, 30, 150, 50), border_radius=5)

        win.blit(txt, (263, 40))

        display(win, universe)
        
        pygame.time.wait(350)

        universe = next_generation(universe)



