'''
env.reset()
env.step(action) returns next_state,reward,done
env.render()
'''

import env
import random

def reset():
    board.shuffle(100)
    # print(board)
    return board

def manhattan_distance(state):
    state = [j for sub in state for j in sub]
    for i in range(len(state)):
        if state[i] == '*':
            state[i] = 0
    # print(state)
    d = sum(abs((val-1)%4 - i%4) + abs((val-1)//4 - i//4) for i, val in enumerate(state) if val)
    return d
    
# def calculate_reward(state):
#     final_state = board.goal
#     punish = 0
#     for i in range(4):
#         for j in range(4):
#             if state[i][j] != final_state[i][j]:
#                 punish += 1
#             # else:
#             #     reward -= 1
#     reward = 16-punish
#     return reward


def step(action): 
    if action == 1:             #up
        board.move_up()
    elif action == 2:           #down
        board.move_down()
    elif action == 3:           #left
        board.move_left()
    else:                       #right
        board.move_right()
    
    next_state = board.get_state()
    # reward = calculate_reward(next_state)
    reward = manhattan_distance(next_state)
    done = False
    if reward == 16:
        done = True

    return next_state, reward, done    

board = env.Board()
board.shuffle(100)
print(board.get_state())
# print(step(2))
state = board.get_state()
print(manhattan_distance(state))
