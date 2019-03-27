from time import sleep
from growing_tree import generate
from A_star import astar
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (240, 128, 128)
GREEN = (0, 255, 127)

def createScreen():
    screen_width, screen_height = pygame.display.list_modes(0)[0]
    flags = pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF

    screen = pygame.display.set_mode(
            (screen_width, screen_height), flags)
    print("screen size: ", screen.get_size())

def draw_maze(x, y, block_size):
    x *= block_size
    y *= block_size
    pygame.draw.rect(screen, WHITE, (x, y, block_size, block_size))

def draw_path(x, y, block_size):
    x *= block_size
    y *= block_size
    pygame.draw.rect(screen, RED, (x, y, block_size, block_size))

def traceack(x, y, block_size):
    x *= block_size
    y *= block_size
    center = ((x + block_size // 2)), (y + (block_size // 2))
    pygame.draw.circle(screen, alive_color, center, block_size // 2,0)

def handleInputEvents():
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN):
            if (event.button == 1):
                # Create wall at coord clicked
        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                exit(0)
        elif (event.type == pygame.QUIT):
            print("quitting")
            exit(0)

def main():
    global screen

    pygame.init()
    pygame.display.set_caption("Maze Traversal")
    clock = pygame.time.Clock()
    screen = createScreen()
    (xmax,ymax) = screen.get_size()
    xlen = xmax // 9
    ylen = ymax // 9

    block_size = 9
    
    maze = generate(xmax, ymax)

    while True:
        handleInputEvents()
        for x in range(xlen):
            for y in range(ylen):
                draw_maze(maze)
                draw_path()
                traceback()
                
                clock.tick(60)
        pygame.display.flip()

    start = (0, 0)
    end = (0, 9)

    path = astar(maze, start, end)
    print(path)

main()
