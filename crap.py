import gym
import numpy as np
# from puzzle8 import *
env = gym.make('CartPole-v1')
# env = Puzzle8()
state = env.reset()
# state = np.reshape(state,9,1)
state = np.array([state])
print(state)
