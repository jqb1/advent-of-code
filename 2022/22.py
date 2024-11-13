import re
from collections import deque


def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


DIRECTION = {
    "l": (0, -1),
    "r": (0, 1),
    "u": (-1, 0),
    "d": (1, 0),
}

DRAW = {
    "l": "<",
    "r": ">",
    "u": "^",
    "d": "v",
}

# direction facing, turn: new direction
TURN = {
    ("r", "R"): "d",
    ("r", "L"): "u",
    ("l", "L"): "d",
    ("l", "R"): "u",
    ("u", "R"): "r",
    ("u", "L"): "l",
    ("d", "L"): "r",
    ("d", "R"): "l",
}


def main():
    position = (0, 50)
    direction = "r"
    puzzle = read_input()
    grid = [list(l) for l in puzzle[:-1]][:-1]
    max_row = max(len(r) for r in grid)
    for row in grid:
        if len(row) < max_row:
            row.extend([" "] * (max_row - len(row)))

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
            continue

        position, direction = move(move_cnt, direction, position, grid)

        # for r in grid:
        #     print(' '.join([c for c in r]))

    facing = {"r": 0, "d": 1, "l": 2, "u": 3}
    grid[position[0]][position[1]] = "E"
    for r in grid:
        print(" ".join([c for c in r]))
    final_r, final_c = position[0] + 1, position[1] + 1
    print(final_r, final_c, direction)
    print(1000 * final_r + 4 * final_c + facing[direction])


def move(move_cnt, direction, position, grid):
    max_r, max_c = len(grid), len(grid[0])
    pos_r, pos_c = position
    dr, dc = DIRECTION[direction]

    for i in range(move_cnt):
        if (
            pos_r + dr == max_r
            or pos_c + dc == max_c
            or pos_c + dc == -1
            or pos_r + dr == -1
            or grid[pos_r + dr][pos_c + dc] == " "
        ):
            new_pos_r, new_pos_c, new_direction = wrap_side(
                (pos_r, pos_c), direction, grid
            )
            print(pos_r, pos_c, direction, "   ", new_pos_r, new_pos_c, new_direction)
            if new_pos_c == pos_c and new_pos_r == pos_r and new_direction == direction:
                break
            pos_r, pos_c, direction = new_pos_r, new_pos_c, new_direction
            grid[pos_r][pos_c] = DRAW[direction]
            dr, dc = DIRECTION[direction]
            continue
        if grid[pos_r + dr][pos_c + dc] == "#":
            return (pos_r, pos_c), direction
        pos_r, pos_c = pos_r + dr, pos_c + dc
        grid[pos_r][pos_c] = DRAW[direction]

    return (pos_r, pos_c), direction


def wrap_side(position, direction, grid):
    cur_r, cur_c = position
    start_r, start_c = position
    old_direction = direction
    # dr, dc = DIRECTION[direction]

    max_r, max_c = len(grid), len(grid[0])
    cur_r, cur_c, direction = wrap_cube(position, direction)
    assert grid[cur_r][cur_c] != " "
    # cur_r, cur_c = (cur_r + dr) % max_r, (cur_c + dc) % max_c
    # while grid[cur_r][cur_c] == ' ':
    #     cur_r, cur_c = (cur_r + dr) % max_r, (cur_c + dc) % max_c

    if grid[cur_r][cur_c] == "#":
        return start_r, start_c, old_direction
    return cur_r, cur_c, direction


def wrap_cube(position, direction):
    side_size = 50
    square_row, cur_row = divmod(position[0], side_size)
    square_col, cur_col = divmod(position[1], side_size)

    def get_square(r, c, d, row, col):
        # square(row, col), direction: square(row,col), inside square(row, col), direction
        return {
            (0, 1, "u"): (3, 0, (col, 0), "r"),
            (3, 0, "l"): (0, 1, (0, row), "d"),
            (0, 1, "l"): (2, 0, (side_size - row - 1, 0), "r"),
            (2, 0, "l"): (0, 1, (side_size - row - 1, 0), "r"),
            (0, 2, "u"): (3, 0, (side_size - 1, col), "u"),
            (3, 0, "d"): (0, 2, (0, col), "d"),
            (0, 2, "r"): (2, 1, (side_size - row - 1, side_size - 1), "l"),
            (2, 1, "r"): (0, 2, (side_size - row - 1, side_size - 1), "l"),
            (0, 2, "d"): (1, 1, (col, side_size - 1), "l"),
            (1, 1, "r"): (0, 2, (side_size - 1, row), "u"),
            (1, 1, "l"): (2, 0, (0, row), "d"),
            (2, 0, "u"): (1, 1, (col, 0), "r"),
            (2, 1, "d"): (3, 0, (col, side_size - 1), "l"),
            (3, 0, "r"): (2, 1, (side_size - 1, row), "u"),
        }[r, c, d]

    sq_r, sq_c, sq_pos, new_dir = get_square(
        square_row, square_col, direction, cur_row, cur_col
    )
    cur_r = sq_r * side_size + sq_pos[0]
    cur_c = sq_c * side_size + sq_pos[1]
    return cur_r, cur_c, new_dir


if __name__ == "__main__":
    main()
    # assert wrap_cube((0, 52), 'u') == (152, 0, 'r')
    # assert wrap_cube((0, 50), 'l') == (149, 0, 'r')
    # assert wrap_cube((101, 99), 'r') == (48, 149, 'l')
    # assert wrap_cube((101, 0), 'l') == (48, 50, 'r')
    # assert wrap_cube((150, 49), 'r') == (149, 50, 'u')
