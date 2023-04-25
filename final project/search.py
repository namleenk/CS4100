#from snake2 import snake #, visualize_search
import random
from snake import manhattanHeuristic, nullHeuristic, snake, euclideanHeuristic
from util import Stack, Queue, PriorityQueue
import time


# Depth-first search algorithm
def dfs(snake: snake):
    """
    - go down the deepest path to find the food
    - remove the top thing from the stack (LIFO)
    - if the removed state is the goal state, return the path of actions including the final action
    it took to get to the goal state
    - else, if we haven't visited the state yet then add it to the list of visited states
        -- get the successors of the state
        -- for every successor, if its not in the list of visited states then add the action it took
        to get to this state, to the list of actions that represents the path
    - at the end, return the complete path

    """
    stack = Stack()
    visited = set()
    actions = []

    total_length = 0
    num_paths = 0
    num_actions = 0

    startState = snake.getStartState()
    stack.push((startState, []))

    # while the stack is not empty, go through the states and their successors
    while not stack.isEmpty():
        state, path = stack.pop()

        # if we've reached the goal state, calculate the length of the path and continue to the return
        # the average lenght of the path
        if snake.isGoalState(state):
            snake.score = len(path)
            total_length += snake.score
            num_paths += 1
            continue
        
        if state not in visited:
            visited.add(state)
            actions.append(path)

            successors = snake.getSuccessors(state)
            random.shuffle(successors)

            for successor in successors:
                if successor[0] not in visited:
                    validState = (successor[0], path + [successor[1]])
                    stack.push(validState)
                    num_actions += 1
                    #print('successor added - dfs')

    if num_paths == 0:
        return 0
    else:
        average_length = total_length / num_paths

    #print('dfs: ', actions[len(actions)-1])
    print('dfs', snake.expanded)
    return average_length

# Breadth-first search algorithm
def bfs(snake: snake):
    """
    - go down the deepest path to find the food
    - remove the top thing from the stack (LIFO)
    - if the removed state is the goal state, return the path of actions including the final action
    it took to get to the goal state
    - else, if we haven't visited the state yet then add it to the list of visited states
        -- get the successors of the state
        -- for every successor, if its not in the list of visited states then add the action it took
        to get to this state, to the list of actions that represents the path
    - at the end, return the complete path

    """
    queue = Queue()
    visited = set()
    actions = []

    total_length = 0
    num_paths = 0
    num_actions = 0

    startState = snake.getStartState()
    queue.push((startState, []))

    # while the stack is not empty, go through the states and their successors
    while not queue.isEmpty():
        state, path = queue.pop()

        # if we've reached the goal state, calculate the length of the path and continue to the return
        # the average lenght of the path
        if snake.isGoalState(state):
            snake.score = len(path)
            total_length += snake.score
            num_paths += 1
            continue
        
        if state not in visited:
            visited.add(state)
            actions.append(path)

            successors = snake.getSuccessors(state)
            random.shuffle(successors)

            for successor in successors:
                if successor[0] not in visited:
                    validState = (successor[0], path + [successor[1]])
                    queue.push(validState)
                    num_actions +=1


    if num_paths == 0:
        return 0
    else:
        average_length = total_length / num_paths

    #print('bfs: ', actions[len(actions)-1])
    print('bfs', snake.expanded)
    return average_length

# Uniform Cost Search algorithm --> all states have the same priority
def ucs(snake: snake):

    priorityQueue = PriorityQueue()
    visited = set()
    actions = []

    total_length = 0
    num_paths = 0
    num_actions = 0

    startState = snake.getStartState()
    #                  (state,    path, cost) priority
    priorityQueue.push((startState, [], 0), 0)

    while not priorityQueue.isEmpty():
        (state, path, cost) = priorityQueue.pop()

        if snake.isGoalState(state):
            snake.score = len(path)
            total_length += snake.score
            num_paths += 1
            continue

        if state not in visited:
            visited.add(state)
            actions.append(path)

            successors = snake.getSuccessors(state)
            random.shuffle(successors)

            for successor in successors:
                if successor[0] not in visited:
                    validState = (successor[0], path + [successor[1]], cost + successor[2])
                    priorityQueue.push(validState, cost + successor[2])
                    num_actions += 1
    
    if num_paths == 0:
        return 0
    else:
        average_length = total_length / num_paths

    #print('ucs: ', actions[len(actions)-1])
    print('ucs', snake.expanded)
    return average_length

def astar(snake: snake, heuristic):
    
    priorityQueue = PriorityQueue()
    visited = set()
    actions = []

    total_length = 0
    num_paths = 0

    startState = snake.getStartState()
    #                  (state,    path, cost) priority
    priorityQueue.push((startState, [], 0), 0)

    while not priorityQueue.isEmpty():
        (state, path, cost) = priorityQueue.pop()

        if snake.isGoalState(state):
            snake.score = len(path)
            total_length += snake.score
            num_paths += 1
            continue

        if state not in visited:
            visited.add(state)
            actions.append(path)

            successors = snake.getSuccessors(state)
            random.shuffle(successors)

            for successor in successors:
                if successor[0] not in visited:
                    newCost = cost + successor[2]
                    validState = (successor[0], path + [successor[1]], newCost)
                    priorityQueue.push(validState, (heuristic(successor[0], snake.food.pos) + newCost))
    
    if num_paths == 0:
        return 0
    else:
        average_length = total_length / num_paths

    #print('astar: ', actions[len(actions)-1])
    print('astar', snake.expanded)
    return average_length

s = snake((10, 10))

food_list = []
# generate a list of food at random location
def gen_food_list():
    for f in range(0, 400):
        foodx = random.randrange(19)
        foody = random.randrange(19)
        food = (foodx, foody)
        food_list.append(food)

# gen_food_list()
# total_average_length_dfs = 0
# total_average_length_bfs = 0
# total_average_length_ucs = 0
# total_average_length_astar = 0
# astar_euclidean = 0
# dfs_time = 0
# num_iterations = len(food_list)
# for i in range(0, len(food_list)):
#     average_length_dfs = dfs(s)
#     average_length_bfs = bfs(s)
#     average_length_ucs = ucs(s)
#     average_length_astar = astar(s, manhattanHeuristic)
#     average_length_euclidean = astar(s, euclideanHeuristic)

#     total_average_length_dfs += average_length_dfs
#     total_average_length_bfs += average_length_bfs
#     total_average_length_ucs += average_length_ucs
#     total_average_length_astar += average_length_astar
#     astar_euclidean += average_length_euclidean


# print("Average length of DFS:", round(total_average_length_dfs / num_iterations))
# print("Average length of BFS:", round(total_average_length_bfs / num_iterations))
# print("Average length of UCS:", round(total_average_length_ucs / num_iterations))
# print("Average length of A* with manhattan heuristic:", round(total_average_length_astar / num_iterations))
# print("Average length of A* with euclidean heuristic:", round(astar_euclidean / num_iterations))


# prints out the list of directions each algorithm would take
# (uncomment lines 256-260 to view these lists as well as the print statements prior to the return statement in each function)
for i in range(0, 100):
    dfs(s)
    bfs(s)
    ucs(s)
    astar(s, manhattanHeuristic)
    astar(s, euclideanHeuristic)
