import sys
from itertools import product


def read_input():
    with open("./input.txt") as f:
        moves = [line.rstrip() for line in f]
    return moves


def check_winner(brd):
    if any(all(n == "x" for n in row) for row in brd):
        return True
    if any(all(n == "x" for n in col) for col in zip(*brd)):
        return True


print(read_input())
boards = read_input()
numbers = read_input()[0]
boards = boards[2:]

all_boards = []
single_board = []
for row in boards:
    if row != "":
        single_board.append(list(map(int, row.split())))
    else:
        all_boards.append(single_board)
        single_board = []

for num in map(int, numbers.split(",")):
    to_remove = []
    for board in all_boards:
        sum = 0
        for i, j in product(range(len(board[0])), range(len(board))):
            if board[i][j] != "x":
                sum += board[i][j]
            if board[i][j] == num:
                board[i][j] = "x"

        if check_winner(board):
            sum -= num
            if len(all_boards) == 1:
                print("sum")
                print(sum * num)
                sys.exit(0)
            to_remove.append(board)
            if len(all_boards) == 1:
                print(all_boards[0])

    if to_remove:
        for t in to_remove:
            all_boards.remove(t)
