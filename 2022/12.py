from collections import deque, defaultdict


def read_input():
    with open("/Users/jkoziol/Downloads/input_t.txt") as f:
        moves = [line_.rstrip() for line_ in f]
    return moves


def find_E_and_S(grid_):
    E = None
    S = None
    for r in range(len(grid_)):
        for c in range(len(grid_[0])):
            if grid_[r][c] == "S":
                S = (r, c)
            elif grid_[r][c] == "E":
                E = (r, c)
            if E and S:
                return E, S


DIRECTIONS = {
    "l": (0, -1),
    "r": (0, 1),
    "u": (-1, 0),
    "d": (1, 0),
}


def explore_roads(root_, grid_, e_point_):
    rc, cc = len(grid_), len(grid_[0])
    fewest_steps = rc * cc * 100000  # init max
    path = {
        (root_[0], root_[1]),
    }
    q = deque([root_])

    grid_[e_point_[0]][e_point_[1]] = "z"
    while q:
        curr_point = q.popleft()
        curr_r, curr_c, p_len = curr_point
        print(curr_r, curr_c, grid_[curr_r][curr_c], p_len)
        if (curr_r, curr_c) == e_point_:
            return p_len

        for dr, dc in DIRECTIONS.values():
            point_r = curr_r + dr
            point_c = curr_c + dc
            if 0 <= point_r < rc and 0 <= point_c < cc:
                if (
                    ord(grid_[point_r][point_c]) <= ord(grid_[curr_r][curr_c]) + 1
                ) or grid_[curr_r][curr_c] == "S":
                    if not (point_r, point_c) in path:
                        path.add((point_r, point_c))
                        q.append((point_r, point_c, p_len + 1))


def main():
    grid = [list(r) for r in read_input()]
    print(grid)

    e_point, s_point = find_E_and_S(grid)
    print(e_point, s_point)
    s_point = (s_point[0], s_point[1], 0)

    shortest = 9000
    # part 1 without this loop
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "a":
                result = explore_roads(s_point, grid, e_point)
                if result and result < shortest:
                    shortest = result

    print(shortest)


if __name__ == "__main__":
    main()
