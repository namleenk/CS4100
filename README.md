# CS4100
Final project for CS4100: Artificial Intelligence

Welcome to my Snake AI!

This repository contains a backend implementation of Snake. Additionally, there are a couple of files for the AI that can play Snake. The following explains each of the files:
  * The snake.py file implements the backend of the game Snake. The most important part of this file is the three methods that handle the states of the game, getting the start state, checking if a state is one of the goal states of food, and getting the list of successors of the current state. This file also contains a few heuristics that are used in one of the search algorithms.

  * The util.py file contains implementations for data structures used in the search algorithms.

  * The search.py file is the AI of the game where the snake finds paths to the food(s) using various search algorithms. The four search algorithms implemented are depth-first, breadth-first, uniform cost, and A* search. A* search notably uses the heuristics such as the Manhattan and Euclidean heuristics to find the optimal path(s).


The purpose of this Snake AI is to compare the search algorithms in terms of the average length of the path to food (across all possible locations of the food), the list of actions taken, and the number of states expanded. You can use the following steps to run the code (assuming you have python3 installed):
* Download and set up the snake.py, util.py, and search.py files.
* Enter the `final project` directory.
* Run one of the following commands:
  1. python3 search.py --comparator 'path_length'
  2. python3 search.py --comparator 'actions'
  3. python3 search.py --comparator 'states'


Heuristics:
* Manhattan heuristic: The Manhattan heuristic calculates the Manhattan distance between two points which is the straight line distance in either the horizontal or vertical direction.

* Euclidean heuristic: The Euclidean heuristic calculates the Euclidean distance between two points which is the straight line distance in either the horizontal, vertical, or diagonal direction.

Comparison: Both heuristics result in the same average path length and length of the list of actions taken. However, the Manhattan heuristic expanded fewer states than the Euclidean heuristic because it only considers movement in the horizontal and vertical directions whereas the Euclidean heuristic adds movement in the diagonal direction.