# def manhatan_dist(board,goal):
#     return sum(abs(b%3 - g%3) + abs(b//3 - g//3) for b, g in ((board.index(i), goal.index(i)) for i in range(1, 9)))


import numpy as np

# [[5 1 6]
#  [2 4 9]
#  [8 7 3]]
g = np.reshape(np.array([[1,2,3],[4,5,6],[7,8,9]]),(1,9))[0].tolist()
t = 0
for i in range(9):
    t += g[i]*i
print(t)

# print(manhatan_dist(b,g))