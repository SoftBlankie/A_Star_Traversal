from time import sleep
from random import randint
from growing_tree import generate_gt
from A_star import astar
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def createScreen():
    screen_width, screen_height = pygame.display.list_modes(0)[0]
    flags = pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF

    screen = pygame.display.set_mode(
            (screen_width, screen_height), flags)
    print("screen size: ", screen.get_size())
    return screen

'''
Left click : Create or remove wall
Spacebar : Create new maze
Escape : Quit
'''
def handleInputEvents():
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                exit(0)
            elif (event.key == pygame.K_SPACE):
                screen.fill(WHITE)
                runMaze()
        elif (event.type == pygame.QUIT):
            print("quitting")
            exit(0)

def runMaze():
    global maze

    maze = generate_gt(xlen, ylen, screen, block_size, bktrk_chce)
    
    start = (randint(1, 5), randint(1, 5))
    end = (randint(xlen-5, xlen-1), randint(ylen-5, ylen-1))

    while (maze[start[0]][start[1]] == 1):
        start = (randint(1, 5), randint(1, 5))
    while (maze[end[0]][end[1]] == 1):
        end = (randint(xlen-5, xlen-1), randint(ylen-5, ylen-1))

    path = astar(maze, start, end, screen, block_size)

def main():
    global screen, xlen, ylen, start, end, block_size, bktrk_chce

    bktrk_chce = -1
    while (bktrk_chce < 0 or bktrk_chce > 1.0):
        bktrk_chce = float(input("Backtrack chance (0.0 - 1.0): "))

    pygame.init()
    pygame.display.set_caption("Maze Traversal")
    clock = pygame.time.Clock()
    screen = createScreen()
    screen.fill(WHITE)
    (xmax,ymax) = screen.get_size()
    xlen = xmax // 9
    ylen = ymax // 9

    block_size = 9
    
    runMaze()

    while True:
        handleInputEvents()
        clock.tick(60)

        pygame.display.flip()

main()
