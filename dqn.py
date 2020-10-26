# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 00:24:58 2019
@author: Unnikrishnan Menon
"""

import gym
import numpy as np
import random

from keras.models import Sequential
from keras.layers import Activation
from keras.layers import Dense

from puzzle8 import *

env = Puzzle8()

model=Sequential()
model.add(Dense(24,input_dim=9,activation='relu'))
# model.add(Dense(24,activation='relu'))
model.add(Dense(4,activation='relu'))
model.compile(optimizer='Adam',loss='mse',metrics=['mae'])

gamma = 1.0
epsilon = 1.0
m = []

for i in range(5000):
    state = env.reset()
    state = np.reshape(state,9,1)
    state = np.array([state])
    for t in range(200):
        if np.random.rand() <= epsilon:
            action = random.randrange(4)
        else:
            action = np.argmax(model.predict(state))
        next_state,reward,done = env.step(action)
        next_state = np.reshape(next_state,9,1)
        next_state = np.array([next_state])
        tot = reward + gamma * np.max(model.predict(next_state))
        p = model.predict(state)[0]
        p[action] = tot
        model.fit(state, p.reshape(-1, 4), epochs=1, verbose=0)
        m.append((state,action,reward,next_state,done))
        state = next_state
        if done:
            print("Episode : {}, Score: {}, Reward: {}".format(i,t,reward))
            break
        if len(m)==50000:
            del m[:5000]
    if epsilon > 0.01:
        epsilon *= 0.999
    if len(m) > 64:
        for state, action, reward, next_state, done in random.sample(m,64):
            tot=reward
            if not done:
              tot=reward + gamma * np.max(model.predict(next_state))

            p = model.predict(state)[0]
            p[action] = tot
            model.fit(state,p.reshape(-1,4), epochs=1, verbose=0)

for i in range(1):
    state = env.reset()
    state = np.reshape(state,9,1)
    state = np.array([state])
    done = False
    while not done:
        # env.render()
        action = np.argmax(model.predict(state))
        next_state, reward, done, observation = env.step(action)
        print(next_state)
        next_state = np.reshape(next_state,9,1)
        next_state = np.array([next_state])
        state = next_state