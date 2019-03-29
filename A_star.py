import pygame

RED = (240, 128, 128)
GREEN = (0, 255, 127)

class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0 # cost to goal
        self.h = 0 # estimated cost to goal
        self.f = 0 # g + h

    def __eq__(self, other):
        return self.position == other.position

def draw_path(x, y, screen, block_size):
    x *= block_size
    y *= block_size
    pygame.draw.rect(screen, RED, (x, y, block_size, block_size))

def draw_traceback(x, y, screen, block_size):
    x *= block_size
    y *= block_size
    center = ((x + block_size // 2)), (y + (block_size // 2))
    pygame.draw.circle(screen, GREEN, center, block_size // 2, 0)

def handleInputEvents():
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                exit(0)

'''
The A* algorithm traverse and finds the best path towards the start to end.
It uses heuristics and variables, g, h, f in which provides an estimate as
well as exact pathings to reach the end goal. This essentially finds a
pathing that minimizes the distance between the start and end
'''
def astar(maze, start, end, screen, block_size):
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    pygame.draw.rect(screen, GREEN,
            (start[0]*9, start[1]*9, block_size, block_size))
    pygame.draw.rect(screen, GREEN,
            (end[0]*9, end[1]*9, block_size, block_size))

    open_list = [] # list of nodes around current node
    closed_list = [] # list of visited nodes around current node

    open_list.append(start_node)

    # Loop until end node found and all possibilities checked
    while len(open_list) > 0:
        handleInputEvents()

        # Get the current node, node with smallest f value
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list and add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # If end node reached, do traceback
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                handleInputEvents()
                draw_traceback(current.position[0], current.position[1],
                        screen, block_size)
                pygame.display.flip()
                path.append(current.position)
                current = current.parent
            return path[::-1]

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            
            # Get adjacent node position
            node_position = (current_node.position[0] + new_position[0],
                    current_node.position[1] + new_position[1])
            
            # Create new node
            new_node = Node(current_node, node_position)

            # Check if in range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1])-1) or node_position[1] < 0:
                continue

            # Check if traversable
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Check if already visited
            if new_node in closed_list:
                continue

            # Append as potential adjacent
            children.append(new_node)

        # Loop through children and assign node values
        for child in children:
            
            # Skip children unreachable
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) **2) + ((child.position[1] - end_node.position[1]) **2)
            child.f = child.g + child.h

            # Skip higher cost children already in open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            draw_path(child.position[0], child.position[1],
                    screen, block_size)
            pygame.draw.rect(screen, GREEN,
                    (end[0]*9, end[1]*9, block_size, block_size))
            pygame.display.flip()

            open_list.append(child)
