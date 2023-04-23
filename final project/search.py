#from snake2 import snake #, visualize_search
import random
from snake import snake
import util

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
    stack = util.Stack()
    visited = set()

    total_length = 0
    num_paths = 0

    startState = snake.getStartState()
    stack.push((startState, []))

    # while the stack is not empty, go through the states and their successors
    while not stack.isEmpty():
        state, path = stack.pop()

        # if we've reached the goal state, return the path
        if snake.isGoalState(state):
            # move the snake, with path actions, and the food is at snake's current location
 
            # print('score: ', snake.score)
            # print('in goal state check: ', path)
            # print(len(path))
            snake.score = len(path)
            total_length += snake.score
            num_paths += 1
            continue
            #return path
        
        if state not in visited:
            visited.add(state)

            successors = snake.getSuccessors(state)
            random.shuffle(successors)
            #print('successors: ',  successors)

            for successor in successors:
                if successor[0] not in visited:
                    validState = (successor[0], path + [successor[1]])
                    stack.push(validState)

    average_length = total_length / num_paths if num_paths > 0 else 0
    #print('average length: ', average_length)
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
    queue = util.Queue()
    visited = set()

    total_length = 0
    num_paths = 0

    startState = snake.getStartState()
    queue.push((startState, []))

    # while the stack is not empty, go through the states and their successors
    while not queue.isEmpty():
        state, path = queue.pop()

        # if we've reached the goal state, return the path
        if snake.isGoalState(state):
            # move the snake, with path actions, and the food is at snake's current location
 
            # print('score: ', snake.score)
            # print('in goal state check: ', path)
            # print(len(path))
            snake.score = len(path)
            total_length += snake.score
            num_paths += 1
            continue
            #return path
        
        if state not in visited:
            visited.add(state)

            successors = snake.getSuccessors(state)
            random.shuffle(successors)
            #print('successors: ',  successors)

            for successor in successors:
                if successor[0] not in visited:
                    validState = (successor[0], path + [successor[1]])
                    queue.push(validState)

    average_length = total_length / num_paths if num_paths > 0 else 0
    #print('average length: ', average_length)
    return average_length

s = snake((10, 10))

food_list = []
# generate a list of food at random location
def gen_food_list():
    for f in range(0, 399):
        foodx = random.randrange(19)
        foody = random.randrange(19)
        food = (foodx, foody)
        food_list.append(food)

gen_food_list()
total_average_length = 0
num_iterations = len(food_list)
for i in range(0, len(food_list)):
    #average_length = dfs(s)
    average_length = bfs(s)
    total_average_length += average_length

print("Average length of paths:", round(total_average_length / num_iterations))

# # Breadth-first search algorithm -- queue
# # Uniform cost search algorithm -- priority queue, with all priorities = 1
# # A* search algorithm -- priority queue