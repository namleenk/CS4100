import random
import pygame

from util import manhattanDistance

global rows
rows = 20

class cube(object):
    w = 500
    rows = 20
    def __init__(self,start,dirnx=1,dirny=0):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
 
       
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

def randomSnack(rows, item):
 
    positions = item.body
 
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break
    return (x, y)
 
class snake(object):
    body = []
    turns = {}

    def __init__(self, pos):
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1
        self.food = cube(randomSnack(rows, self))
        self.expanded = 0

        # since snake can wrap around the board, the walls analogous to pacman are the snake's body itself
        self.walls = []
        self.walls.append(self.head)
        self.score = 0
    
    def move(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        # added an additional check to make sure the current direction is not the opposite of the key pressed
        if keys[pygame.K_LEFT] and not self.dirnx == 1:
            self.dirnx = -1
            self.dirny = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        elif keys[pygame.K_RIGHT] and not self.dirnx == -1:
            self.dirnx = 1
            self.dirny = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        elif keys[pygame.K_UP] and not self.dirny == 1:
            self.dirnx = 0
            self.dirny = -1
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        elif keys[pygame.K_DOWN] and not self.dirny == -1:
            self.dirnx = 0
            self.dirny = 1
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
 
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                # if snake exits the border of the grid, it comes back from the other side
                if c.dirnx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1:
                    c.pos = (0,c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1:
                    c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0],c.rows-1)
                else:
                    c.move(c.dirnx,c.dirny)

    # function to make the snake move given some actions - for the search algorithms
    def actionMove(self, key):
        if key == 'left' and not self.dirnx == 1:
            self.dirnx = -1
            self.dirny = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        elif key == 'right' and not self.dirnx == -1:
            self.dirnx = 1
            self.dirny = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        elif key == 'up' and not self.dirny == 1:
            self.dirnx = 0
            self.dirny = -1
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        elif key == 'down' and not self.dirny == -1:
            self.dirnx = 0
            self.dirny = 1
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        # same as for the manual move function
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                # if snake exits the border of the grid, it comes back from the other side
                if c.dirnx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1:
                    c.pos = (0,c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1:
                    c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0],c.rows-1)
                else:
                    c.move(c.dirnx,c.dirny)
 
    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

        self.walls = self.body
        self.score = 0
 
 
    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny
 
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
            self.walls = self.body
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
            self.walls = self.body
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
            self.walls = self.body
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1)))
            self.walls = self.body
 
        global all_walls
        all_walls = self.body

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy
    
    def validPos(self, pos):
        rows = 20
        x, y = pos
        if (x < 0 or x > rows-1 or y < 0 or y > rows-1):
            #print('false')
            return False
        if pos in self.walls:
            #print('false - walls')
            return False
        #print('true')
        return True
        
    # return the position of the head of the snake
    def getStartState(self):
        return self.head.pos
    

    # checks if the given state is the goal state, such that the given state is the same as a food location
    def isGoalState(self, curr_pos):
        return curr_pos == self.food.pos
  
    # returns the list of successors of the given state
    def getSuccessors(self, curr_pos):

        walls_pos = []
        for wall in self.walls:
            walls_pos.append(wall)

        successors = []
        actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        directions = ['down', 'up', 'right', 'left']
        #x, y = curr_pos
        x = curr_pos[0]
        y = curr_pos[1]

        for move in actions:
            dx = move[0]
            dy = move[1]
            nextx = int(x + dx)
            nexty = int(y + dy)

            next_pos = (nextx, nexty)
            if (next_pos not in walls_pos) and (next_pos != curr_pos) and (next_pos not in successors) and self.validPos(next_pos):
                if dx == 1:
                    direction = 'right'
                elif dx == -1:
                    direction == 'left'
                elif dy == 1:
                    direction = 'down'
                elif dy == -1:
                    direction = 'up'
                cost = manhattanDistance(curr_pos, next_pos)
                successors.append((next_pos, direction, cost))

        self.expanded += 1
        return successors

# arbitrary heuristic to run the a* search algorithm
def nullHeuristic(s: snake, food: cube):
    return 0

# heuristic to calculate the shortest path distance, in a straight line
def euclideanHeuristic(s: snake, food: cube):
    sx1, sy1 = s
    #fx2, fy2 = food.pos
    fx2, fy2 = food
    return round(((fx2 - sx1) ** 2 + (fy2 - sy1) ** 2) ** 0.5)

def manhattanHeuristic(s: snake, food: cube):
    sx1, sy1 = s
    fx2, fy2 = food
    return round(abs(sx1 - fx2) + abs(sy1 - fy2))

# this shows the actionMove function works -- REMOVE BEFORE SUBMITTING
def showMoves(s):
    global width, rows, snack
    width = 500
    rows = 20
    s = snake((10, 10))
    snack = cube(randomSnack(rows, s))
    clock = pygame.time.Clock()

    directions = ['right', 'right', 'right', 'right', 'right', 'down', 'down', 'down', 'down']
    for dir in directions:
        pygame.time.delay(50)
        clock.tick(10)
        s.action_move(dir)
        print(dir)

s = snake((10, 10))
#showMoves(s)
#s.validPos((7, 15))
foodx = random.randrange(19)
foody = random.randrange(19)
food = (foodx, foody)
