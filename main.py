from env import Board
board = Board()
board.shuffle(20)
print(board)
board.move_left()
board.move_up()
# print(board)
print(board.get_state())