#from snake2 import snake #, visualize_search
import random
from snake2 import snake
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

    startState = snake.getStartState()
    stack.push((startState, []))

    # while the stack is not empty, go through the states and their successors
    while not stack.isEmpty():
        state, path = stack.pop()

        # if we've reached the goal state, return the path
        if snake.isGoalState(state):
            # move the snake, with path actions, and the food is at snake's current location
            snake.score += 1
            snake.addCube()
            #visualize_search(snake, path)
            return path
        
        if state not in visited:
            visited.add(state)

            successors = snake.getSuccessors(state)
            print('successors: ',  successors)

            for successor in successors:
                if successor[0] not in visited:
                    validState = (successor[0], path + [successor[1]])
                    stack.push(validState)
    print(path)
    return path

s = snake((10, 10))
#dfs(s)
# for i in range(0, 10):
#   dfs(s)

food_list = []
def gen_food_list():
    for f in range(0, 399):
        foodx = random.randrange(19)
        foody = random.randrange(19)
        food = (foodx, foody)
        food_list.append(food)

gen_food_list()
for i in range(0, len(food_list)):
    dfs(s)



# path = dfs(s)
# for action in path:
#     s.action_move(action)
    #visualize_search(s, path)


# # Breadth-first search algorithm -- queue
# # Uniform cost search algorithm -- priority queue, with all priorities = 1
# # A* search algorithm -- priority queue