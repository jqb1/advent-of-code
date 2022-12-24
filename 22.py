import re
from collections import deque


def read_input():
    with open("/Users/jkoziol/Downloads/input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


DIRECTION = {
    'l': (0, -1),
    'r': (0, 1),
    'u': (-1, 0),
    'd': (1, 0),
}

DRAW = {
    'l': '<',
    'r': '>',
    'u': '^',
    'd': 'v',
}

# direction facing, turn: new direction
TURN = {
    ("r", "R"): 'd',
    ("r", "L"): 'u',
    ("l", "L"): 'd',
    ("l", "R"): 'u',
    ("u", "R"): 'r',
    ("u", "L"): 'l',
    ("d", "L"): 'r',
    ("d", "R"): 'l',
}


def main():
    position = (0, 8)
    direction = 'r'
    puzzle = read_input()
    grid = [list(l) for l in puzzle[:-1]]
    max_row = max(len(r) for r in grid)
    for row in grid:
        if len(row) < max_row:
            row.extend([' ']*(max_row - len(row)))

    steps = re.split(r"(\d+)", puzzle[-1])[1:-1]
    steps = deque(steps)
    print(steps)

    grid[position[0]][position[1]] = "o"

    while steps:
        step = steps.popleft()
        move_cnt = 0
        if step.isnumeric():
            move_cnt = int(step)
        else:
            direction = TURN[(direction, step)]

        position = move(move_cnt, direction, position, grid)

        for r in grid:
            print(' '.join([c for c in r]))

    facing = {
        'r': 0,
        'd': 1,
        'l': 2,
        'u': 3
    }
    final_r, final_c = position[0] + 1, position[1] + 1

    print(1000*final_r + 4*final_c + facing[direction])


def move(move_cnt, direction, position, grid):
    max_r, max_c = len(grid), len(grid[0])
    pos_r, pos_c = position
    dr, dc = DIRECTION[direction]

    for i in range(move_cnt):
        if pos_r + dr == max_r or pos_c + dc == max_c or grid[pos_r + dr][pos_c + dc] == ' ':
            pos_r, pos_c = wrap_side((pos_r, pos_c), direction, grid)
            grid[pos_r][pos_c] = DRAW[direction]
            continue
        if grid[pos_r + dr][pos_c + dc] == '#':
            return pos_r, pos_c
        pos_r, pos_c = pos_r + dr, pos_c + dc
        grid[pos_r][pos_c] = DRAW[direction]

    return pos_r, pos_c


def wrap_side(position, direction, grid):
    cur_r, cur_c = position
    start_r, start_c = position
    dr, dc = DIRECTION[direction]

    max_r, max_c = len(grid), len(grid[0])
    cur_r, cur_c = (cur_r + dr) % max_r, (cur_c + dc) % max_c
    while grid[cur_r][cur_c] == ' ':
        cur_r, cur_c = (cur_r + dr) % max_r, (cur_c + dc) % max_c
    if grid[cur_r][cur_c] == "#":
        return start_r, start_c
    return cur_r, cur_c



if __name__ == "__main__":
    main()
