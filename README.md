# conway_game_of_life
Author: Anshar_Shampoo \
This is a simple implementation of Conway's Game of Life in Python and pygame. 

![acimsp11](https://github.com/AnsharShampoo/conway_game_of_life/blob/main/achimsp11.png)
## What is Conway's Game of Life? 
The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. [Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
### Rules
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

## How to play
1. Clone the repository
2. Install the required packages using `pip install -r requirements.txt`
3. Run the game using `python conway_game.py`on the terminal
4. Click on the cells to make them alive or dead
5. Press `space` to start the game
6. Press `space` again to reset the game

## Patch Notes

### v0.1
The game can run only on an m x n grid, if you want to change the grid size, you have to change the code in the `conway_game.py` file, specifically the `size` variable in the main function.
