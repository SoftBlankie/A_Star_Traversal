# Maze traversal

Maze traversal using Python and Pygame

![keyword]()

This program implements its own maze generator as well as solver. Currently implemented is the growing tree maze generator and the A* maze traverser.

### Goal

The goal of this program for me is to understand how maze traversal works and how mazes are generated. From this, I'm better able to understand how pathings are made as well as how maps such as Google maps are created. The project also allows for me to understand the A* algorithm, other solving algorithms, as well as maze generation algorithms and their applications. Furthermore understanding how to implement graphics within Pygame.

### Features

Users are able to input a backtrack chance for variations in creating a maze. Simply, inputting 0.0 returns longer pathways and inputting 1.0 returns more random mazes. The reason being that the growing tree algorithm allows for greater diversity in how mazes are generated. 0.0 being more like the backtracking algorithm and 1.0 being more like prim's algorithm.

Users are able to see how the algorithms generate each step within the maze. White indicating the walls of the maze while black indicates the pathings within the maze. Once the maze is generated, the program applies the A* algorithm to find the best path from a randomized start and end. Red pathing within the maze indicates the algorithm's attempt at reaching the end while green dots indicate the traceback on finding the best path from the start to end.

### Controls

Keys:  
Escape : Quit  
Spacebar : Create new maze

### Reference

Some references involve understanding concepts and coder's implementation while optimizing it for its use in this program.

#### Maze Generation

[theJollySin](https://github.com/theJollySin)  
[Jamis](http://weblog.jamisbuck.org/)  

#### A* algorithm

[John Levine](https://www.youtube.com/watch?v=6TsL96NAZCo)  
[Nicholas Swift](https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2)  
