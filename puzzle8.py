import numpy as np
import math


class Puzzle8:
    def __init__(self):
        self.grid = self.reset()
        self.target = np.array([[1,2,3],[4,5,6],[7,8,0]])
        self.action_space = [0,1,2,3] #[up,down,left,right]
        self.done = False
        self.reward = self.fitness()
        self.counter = 0

    def reset(self):
        self.counter = 0
        self.done = False
        temp = np.array([1,2,3,4,5,6,7,8,9])
        np.random.shuffle(temp)
        self.grid = np.reshape(temp,(3,3))
        return self.grid

    def fitness(self):
        b = np.reshape(self.grid,(1,9))[0].tolist()
        # g = np.reshape(self.target,(1,9))[0].tolist()
        # return manhatan_dist(b,g)
        return ringsyourbells(b)

    def render(self):
        print(self.grid)
        print('\n')

    def step(self,action):
        i,j = get_pos(self.grid)
        if action == 0 and i!=0:
            temp = self.grid[i-1][j]
            self.grid[i-1][j] = self.grid[i][j]
            self.grid[i][j] = temp
            # self.counter += 1
            
        elif action == 1 and i!=2:
            temp = self.grid[i+1][j]
            self.grid[i+1][j] = self.grid[i][j]
            self.grid[i][j] = temp
            # self.counter += 1
            
        elif action == 2 and j!=0:
            temp = self.grid[i][j-1]
            self.grid[i][j-1] = self.grid[i][j]
            self.grid[i][j] = temp
            # self.counter += 1
            
        elif action == 3 and j!=2:
            temp = self.grid[i][j+1]
            self.grid[i][j+1] = self.grid[i][j]
            self.grid[i][j] = temp
            # self.counter += 1

        self.counter += 1

        self.reward = self.fitness()
        if self.reward == 240 or self.counter>=200:
            self.done = True

        return self.grid, self.reward, self.done


def get_pos(board):
    a = np.argwhere(board == 9)
    i = a[0][0]
    j = a[0][1]
    return i,j

def manhatan_dist(board,goal):
    return sum(abs(b%3 - g%3) + abs(b//3 - g//3) for b, g in ((board.index(i), goal.index(i)) for i in range(1, 9)))

def ringsyourbells(b):
    t = 0
    for i in range(9):
        t += b[i]*i
    return t

# env = Puzzle8()
# print(env.grid)
# for i in range(4):    
#     action = i
#     print('\n')
#     print(env.step(action))
