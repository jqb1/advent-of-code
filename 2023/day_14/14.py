from functools import cache


def read_input():
    with open("./input.txt") as f:
        lines = [[l for l in line.rstrip()] for line in f]
    return lines


DIRECTIONS = {
    "n": (-1, 0),
    "w": (0, -1),
    "s": (1, 0),
    "e": (0, 1),
}

input_ = read_input()
pos_map = {
    (row, col): input_[row][col]
    for col in range(len(input_[0]))
    for row in range(len(input_))
}
CYCLES_N = 1000000000


def solve():
    row_len, col_len = len(input_), len(input_[0])
    seen = {}
    i = 0
    while i < CYCLES_N:
        tilt_n(row_len, col_len)
        tilt_w(row_len, col_len)
        tilt_s(row_len, col_len)
        tilt_e(row_len, col_len)
        tp = tuple(pos_map.items())
        if tp in seen:
            prev_i = seen[tp]
            repeat_cycle = i - prev_i
            multiplier = (CYCLES_N - i) // repeat_cycle
            print("seen", i, prev_i)
            i = i + repeat_cycle * multiplier
            seen.clear()
        else:
            seen[tp] = i
        i += 1
    c = 0
    for pos, el in pos_map.items():
        if el == "O":
            c += len(input_) - pos[0]
    print(c)


def print_map(i, row_len, col_len, dir_):
    print(f"-----------{i + 1, dir_}-----------")
    for r in range(row_len):
        row = ""
        for col in range(col_len):
            row += f" {pos_map[(r, col)]}"
        print(row)


def tilt_n(row_len, col_len):
    for row in range(row_len):
        for col in range(col_len):
            if pos_map[(row, col)] == "O":
                move((row, col), "n", row_len, col_len)


def tilt_w(row_len, col_len):
    for col in range(col_len):
        for row in range(col_len):
            if pos_map[(row, col)] == "O":
                move((row, col), "w", row_len, col_len)


def tilt_s(row_len, col_len):
    for row in range(row_len)[::-1]:
        for col in range(col_len):
            if pos_map[(row, col)] == "O":
                move((row, col), "s", row_len, col_len)


def tilt_e(row_len, col_len):
    for col in range(col_len)[::-1]:
        for row in range(col_len):
            if pos_map[(row, col)] == "O":
                move((row, col), "e", row_len, col_len)


def move(pos, direction, row_len, col_len):
    row, col = pos
    di, dj = DIRECTIONS[direction]
    while 0 <= row + di < row_len and 0 <= col + dj < col_len:
        if pos_map[(row + di, col + dj)] == ".":
            pos_map[(row, col)] = "."
            row += di
            col += dj
            pos_map[(row, col)] = "O"
        else:
            break


solve()
