from collections import deque, namedtuple


def read_input():
    with open("./input.txt") as f:
        lines = [[field for field in line.rstrip()] for line in f]
    return lines


MAX_STEPS = 262
DIRECTION = {
    "s": (1, 0),
    "n": (-1, 0),
    "w": (0, -1),
    "e": (0, 1),
}
Point = namedtuple("Point", "row, col")


def solve():
    map_ = read_input()
    max_row, max_col = len(map_) - 1, len(map_[0]) - 1
    s_point = Point((max_row + 1) // 2, (max_col + 1) // 2)
    garden_plots = set()
    map_cords = Point(1, 0)
    # map coordinates, point on map, steps
    q = deque([(map_cords, s_point, 0)])
    seen = set()

    while q:
        map_cords, cur_p, steps = q.popleft()
        if (map_cords, cur_p, steps) in seen:
            continue

        seen.add((map_cords, cur_p, steps))
        # print(steps, len(garden_plots))
        if steps == MAX_STEPS:
            garden_plots.add((map_cords, cur_p))
            continue
        for _, (dr, dc) in DIRECTION.items():
            new_p = Point(cur_p.row + dr, cur_p.col + dc)
            if (
                new_p.row > max_row
                or new_p.row < 0
                or new_p.col > max_col
                or new_p.col < 0
            ):
                continue
                # new_p, new_map_cords = wrap_up_map(new_p, map_cords, max_row, max_col)
                # if map_[new_p.row][new_p.col] in {".", "S"}:
                #     q.append((new_map_cords, new_p, steps + 1))
            elif map_[new_p.row][new_p.col] in {".", "S"}:
                q.append((map_cords, new_p, steps + 1))

    print(len(garden_plots))


def wrap_up_map(point, map_cords, max_row, max_col):
    if point.row > max_row:
        return Point(0, point.col), Point(map_cords.row + 1, map_cords.col)
    elif point.row < 0:
        return Point(max_row, point.col), Point(map_cords.row - 1, map_cords.col)
    elif point.col > max_col:
        return Point(point.row, 0), Point(map_cords.row, map_cords.col + 1)
    elif point.col < 0:
        return Point(point.row, max_col), Point(map_cords.row, map_cords.col - 1)


solve()
