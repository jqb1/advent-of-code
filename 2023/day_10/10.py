def read_input():
    with open("./input.txt") as f:
        lines = [[ch for ch in line.rstrip()] for line in f]
    return lines


def pipe_redirect(cur_dir, i, j, pipe):
    if pipe == "|":
        di, dj = DIRECTION[cur_dir]
        if cur_dir in {"u", "d"}:
            return i + di, j + dj, cur_dir
        return
    elif pipe == "-":
        di, dj = DIRECTION[cur_dir]
        if cur_dir in {"r", "l"}:
            return i + di, j + dj, cur_dir
        return
    elif pipe == "L":
        if cur_dir == "l":
            return i - 1, j, "u"
        elif cur_dir == "d":
            return i, j + 1, "r"
        return
    elif pipe == "J":
        if cur_dir == "d":
            return i, j - 1, "l"
        elif cur_dir == "r":
            return i - 1, j, "u"
        return
    elif pipe == "7":
        if cur_dir == "r":
            return i + 1, j, "d"
        elif cur_dir == "u":
            return i, j - 1, "l"
    elif pipe == "F":
        if cur_dir == "u":
            return i, j + 1, "r"
        elif cur_dir == "l":
            return i + 1, j, "d"
        return
    return


DIRECTION = {
    "l": (0, -1),
    "r": (0, 1),
    "u": (-1, 0),
    "d": (1, 0),
}

row_bounds = {}


def solve():
    pipes = read_input()
    # | is a vertical pipe connecting north and south.
    # - is a horizontal pipe connecting east and west.
    # L is a 90-degree bend connecting north and east.
    # J is a 90-degree bend connecting north and west.
    # 7 is a 90-degree bend connecting south and west.
    # F is a 90-degree bend connecting south and east.
    # . is ground; there is no pipe in this tile.
    # S is the starting position of the animal; there is a pipe on this
    s_i, s_j = 0, 0
    for i, row in enumerate(pipes):
        for j in range(len(row)):
            if pipes[i][j] == "S":
                s_i, s_j = (i, j)
                break
    directions = []
    path_pos = []
    loop = {(s_i, s_j)}
    for dir_, delta in DIRECTION.items():
        di, dj = delta
        if new_step := pipe_redirect(
            dir_, s_i + di, s_j + dj, pipes[s_i + di][s_j + dj]
        ):
            ci, cj, cd = new_step
            path_pos.append((ci, cj))
            directions.append(cd)
            loop.update({(ci, cj), (s_i + di, s_j + dj)})

    dist = 2
    while True:
        if path_pos[0] == path_pos[1]:
            pipes[s_i][s_j] = "L"
            return dist, path_pos[0], pipes, loop
        # for each path
        for i, dir_pos in enumerate(zip(directions, path_pos)):
            dir_, pos = dir_pos
            ci, cj, cd = pipe_redirect(dir_, pos[0], pos[1], pipes[pos[0]][pos[1]])
            directions[i] = cd
            path_pos[i] = (ci, cj)
            loop.add((ci, cj))
        dist += 1


def solve_2(pipes, loop):
    c = 0
    for i, row in enumerate(pipes):
        for j in range(len(row)):
            if pipes[i][j] == "." or (i, j) not in loop:
                if check_closed(i, j + 1, pipes[i], loop):
                    c += 1
    print(c)


def check_closed(row_i, col_start, row, loop):
    # if the number of opening/closing pipes is odd it means we are inside
    # crossing number method
    c = 0
    for col_i in range(col_start, len(row)):
        if row[col_i] in {"|", "L", "J"} and (row_i, col_i) in loop:
            c += 1
    return c % 2


p1, path_pos1, pipes, loop = solve()
print(p1, path_pos1)
solve_2(pipes, loop)
