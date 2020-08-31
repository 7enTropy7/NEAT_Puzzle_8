import random
import numpy as np

class Board:

    def __init__(self):
        self.state = np.array([[i for i in range(1, 5)], [i for i in range(5, 9)], [i for i in range(9, 13)], [i for i in range(13, 16)] + ['0']],dtype=int)
        self.empty = [3, 3]

    def __repr__(self):
        string = ''
        for row in self.state:
            for num in row:
                if len(str(num)) == 1:
                    string += '   ' + str(num)
                elif len(str(num)) > 1:
                    string += '  ' + str(num)
            string += '\n'
        return string

    def move_up(self): # move empty block up
        try:
            if self.empty[0] != 0:
                tmp = self.state[self.empty[0]-1][self.empty[1]]
                self.state[self.empty[0]-1][self.empty[1]] = 0
                self.state[self.empty[0]][self.empty[1]] = tmp
                self.empty = [self.empty[0]-1, self.empty[1]]
        except IndexError:
            pass

    def move_down(self): # move empty block down
        try:
            tmp = self.state[self.empty[0]+1][self.empty[1]]
            self.state[self.empty[0]+1][self.empty[1]] = 0
            self.state[self.empty[0]][self.empty[1]] = tmp
            self.empty = [self.empty[0]+1, self.empty[1]]
        except IndexError:
            pass

    def move_right(self): # move empty block right
        try:
            tmp = self.state[self.empty[0]][self.empty[1]+1]
            self.state[self.empty[0]][self.empty[1]+1] = 0
            self.state[self.empty[0]][self.empty[1]] = tmp
            self.empty = [self.empty[0], self.empty[1]+1]
        except IndexError:
            pass

    def move_left(self): # move empty block left
        try:
            if self.empty[1] != 0:
                tmp = self.state[self.empty[0]][self.empty[1]-1]
                self.state[self.empty[0]][self.empty[1]-1] = 0
                self.state[self.empty[0]][self.empty[1]] = tmp
                self.empty = [self.empty[0], self.empty[1]-1]
        except IndexError:
            pass

    def reset(self, steps=100):
        for _ in range(0, steps):
            direction = random.randrange(1, 5)
            if direction == 1:
                self.move_up()
            elif direction == 2:
                self.move_right()
            elif direction == 3:
                self.move_left()
            elif direction == 4:
                self.move_down()

    def step(self,action): 
        m1 = manhattan_distance(self.state.tolist())

        if action == 1:             #up
            self.move_up()
        elif action == 2:           #down
            self.move_down()
        elif action == 3:           #left
            self.move_left()
        else:                       #right
            self.move_right()
        
        m2 = manhattan_distance(self.state.tolist())
        
        reward = m1 - m2
        
        done = False
        if m2 == 0:
            done = True

        return self.state, reward, done   

def manhattan_distance(state):
        state = [j for sub in state for j in sub]
        # for i in range(len(state)):
        #     if state[i] == 0:
        #         state[i] = 0
        # print(state)
        d = sum(abs((val-1)%4 - i%4) + abs((val-1)//4 - i//4) for i, val in enumerate(state) if val)
        return d