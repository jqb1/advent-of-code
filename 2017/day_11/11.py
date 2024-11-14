def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


DIR = {
    # direction to delta row, col
    'n': (0, 2),
    'ne': (1, 1),
    'nw': (-1, 1),
    's': (0, -2),
    'se': (1, -1),
    'sw': (-1, -1),
}
'''
structure: 
    x | 0 | x
    0 | x | 0
    x | 0 | x
'''


def solve():
    inp = read_input()[0].split(',')
    cur_row, cur_col = 0, 0
    max_d = 0
    for step in inp:
        dr, dc = DIR[step]
        cur_row += dr
        cur_col += dc
        cur_d = abs(cur_row) + (abs(cur_col) - abs(cur_row)) / 2
        max_d = max(max_d, cur_d)
    print(max_d)


solve()
