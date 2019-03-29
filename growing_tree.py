from random import choice, shuffle, random, randint
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def make_empty_grid(x, y):
    grid = []
    for i in range(x):
        row = []
        for j in range(y):
            row.append(1)
        grid.append(row)
    return grid

def carve_wall(x, y, screen, block_size):
    wall = grid[x][y]
    cell_color = WHITE if wall else BLACK
    draw_wall(x, y, screen, block_size, cell_color)

def draw_wall(x, y, screen, block_size, cell_color):
    x *= block_size
    y *= block_size
    pygame.draw.rect(screen, cell_color, (x, y, block_size, block_size))

def get_neighbors(x, y, xlen, ylen, grid):
    neighbors = []

    if x > 1 and grid[x-2][y] == 1:
        neighbors.append((x-2, y))
    if x < xlen-2 and grid[x+2][y] == 1:
        neighbors.append((x+2, y))
    if y > 1 and grid[x][y-2] == 1:
        neighbors.append((x, y-2))
    if y < ylen-2 and grid[x][y+2] == 1:
        neighbors.append((x, y+2))

    shuffle(neighbors)

    return neighbors

def handleInputEvents():
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                exit(0)

def generate_gt(xlen, ylen, screen, block_size, bktrk_chce):
    global grid

    # Pick random cell
    grid = make_empty_grid(xlen, ylen)
    x,y = (randint(1, xlen-1), randint(1, ylen-1))
   
    grid[x][y] = 0
    cells = [(x, y)]

    # until no more neighbors
    while cells:
        handleInputEvents()      
        
        if (random() < bktrk_chce):
            x,y = cells[-1]
        else:
            x,y = choice(cells)

        # backtrack to visited
        neighbors = get_neighbors(x, y, xlen, ylen, grid)
        if len(neighbors) == 0:
            cells = [c for c in cells if c != (x, y)]
            continue

        nx,ny = choice(neighbors)
        cells += [(nx, ny)]
        
        grid[nx][ny] = 0
        grid[(x + nx) // 2][(y + ny) // 2] = 0

        carve_wall(x, y, screen, block_size)
        carve_wall(nx, ny, screen, block_size)
        carve_wall((x + nx) // 2, (y + ny) // 2, screen, block_size)

        pygame.display.flip()

    return grid

# Theory
'''
def generate(xlen, ylen):
    # Pick random cell
    grid = make_empty_grid(xlen, ylen)
    x,y = (randint(1, xlen-1), randint(1, ylen-1))
    
    cells = [(x, y)]
   
    # until no more cells
    while cells:
        handleInputEvents()      
        
        # backtrack
        x,y = cells[-1]

        # prim
        #x,y = choice(cells)

        index = True

        # check neighbors
        neighbor_cells = [(x-1, y+0), (x+1, y+0), (x+0,y-1), (x+0,y+1)]
        shuffle(neighbor_cells)
        for nx,ny in neighbor_cells:
            if (nx > 0 and ny > 0 and nx < xlen-1 and ny < ylen-1
                    and grid[nx][ny] == 1):
                grid[x][y] = 0
                grid[nx][ny] = 0
                cells += [(nx, ny)]
                index = False
                break

        if (index):
            cells.remove((x, y))

    return grid
'''
