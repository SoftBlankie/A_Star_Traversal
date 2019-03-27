from random import choice, shuffle, randrange

def make_empty_grid(x, y):
    grid = []
    for i in range(x):
        row = []
        for j in range(y):
            row.append(1)
        grid.append(row)
    return grid

def get_neighbors(x, y, xmax, ymax grid):
    neighbors = []

    if x > 1 and grid[x-2][y] == 1:
        neighbors.append((x-2, y))
    if x < ymax-2 and grid[x+2][y] == 1:
        neighbors.append((x+2, y))
    if y > 1 and grid[x][y-2] == 1:
        neighbors.append((x, y-2))
    if y < xmax-2 and grid[x][y+2] == 1:
        neighbors.append((x, y+2))

    random.shuffle(neighbors)

    return neighbors

def generate(xmax, ymax):
    # Pick random cell
    grid = make_empty_grid(xmax, ymax)
    x,y = (randrange(1, xmax, 2), randrange(1, ymax), 2)
    
    grid[x][y] = 0
    cells = [grid[x][y]]
    
    # until no more neighbors
    while cells:
        x,y = choice(cells)

        # backtrack to visited
        neighbors = get_neighbors(x, y, grid)
        if len(neighbors) == 0:
            cells = [c for c in cells if c != (x, y)]
            continue

        nx,ny = choice(neighbors)
        cells += [(nx, ny)]

        grid[nx][ny] = 0
        grid[(x + nx) // 2][(y + ny) // 2] = 0

    return grid
