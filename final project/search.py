import util

# Depth-first search algorithm
def dfs(board, snake, food):
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
    visited = []

    startState = snake.getStartState()
    stack.push(startState, [])

    # while the stack is not empty, go through the states and their successors
    while not stack.isEmpty():
        state, path = stack.pop()

        # if we've reached the goal state, return the path
        if snake.isGoalState(state):
            return path
        
        if state not in visited:
            visited.append(state)

            successors = snake.getSuccessors(state)

            for successor in successors:
                if successor[0] not in visited:
                    




    # while not stack.isEmpty():
    #     current_state = stack.pop()

    #     if current_state == food:
    #         return get_path







# Breadth-first search algorithm -- queue
# Uniform cost search algorithm -- priority queue, with all priorities = 1
# A* search algorithm -- priority queue