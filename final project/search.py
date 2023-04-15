import util

# Depth-first search algorithm -- stack
def dfs(board, snake, food):
    stack = util.Stack()
    visited = []

    stack.push(snake)

    # while not stack.isEmpty():
    #     current_state = stack.pop()

    #     if current_state == food:
    #         return get_path







# Breadth-first search algorithm -- queue
# Uniform cost search algorithm -- priority queue, with all priorities = 1
# A* search algorithm -- priority queue