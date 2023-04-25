# CS4100
Final project for CS4100: Artificial Intelligence

Welcome to my Snake AI!

This repository contains a backend implementation of snake. Additionally, there are a couple files for the AI that can play Snake. The following explains each of the files:
  * The snake.py file implements the backend of the game Snake. The most important part of this file are three methods that handle the states of the game, getting the start state, checking if a state is one of the goal states of food, and getting the list of successors of the current state. This file also contains a few heuristics which are used one of the search algorithms.

  * The util.py file contains implementations for data structures used in the search algorithms.

  * The search.py file is the AI of the game where the snake finds paths to the food(s) using various search algorithms. The four search algorithms implemented are depth-first, breadth-first, uniform cost, and A* search. A* search notably uses the heuristics such as manhattan and euclidean heuristic to find the optimal path(s).


The purpose of this Snake AI is to compare the search algorithms in terms of the average length of the path to food (across all possible locations of the food), the list of actions taken, and the number of states expanded. You can use the following steps to run the code (assuming you have python3 installed):
* Download and setup the snake.py, util.py, and search.py files.
* Enter the `final project` directory.
* Run one of the following commands:
  1. python3 search.py --comparator path_length
  2. python3 search.py --comparator actions
  3. python3 search.py --comparator states