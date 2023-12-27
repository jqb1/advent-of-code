from collections import defaultdict


def read_input():
    with open("./input.txt") as f:
        lines = [[fld for fld in line.rstrip()] for line in f]
    return lines


directions = ((0, 1), (0, -1), (1, 0), (-1, 0))


def solve(step_limit):
    map_ = read_input()
    height = len(map_)
    s_point = (height // 2, height // 2)
    points = {(0, 0): {s_point}}
    new_points = defaultdict(set)
    for s in range(step_limit):
        for map_c, map_points in points.items():
            for pr, pc in map_points:
                for dr, dc in directions:
                    new_map_c, new_p = wrap_up_map((pr + dr, pc + dc), map_c, height)
                    if map_[new_p[0]][new_p[1]] != "#":
                        new_points[new_map_c].add(new_p)
        print("step", s)
        if (s + 1) % (height // 2 + 2 * height) == 0:
            return new_points, height
        points = new_points
        new_points = defaultdict(set)


def wrap_up_map(point, map_cords, height):
    map_r, map_c = map_cords
    point_r, point_c = point
    if point_r > height - 1:
        map_r += 1
    elif point_c > height - 1:
        map_c += 1
    elif point_c < 0:
        map_c -= 1
    elif point_r < 0:
        map_r -= 1
    return (map_r, map_c), (point_r % height, point_c % height)


if __name__ == "__main__":
    steps_limit = 26501365
    map_to_points, height = solve(steps_limit)
    map_to_points = {k: len(v) for k, v in map_to_points.items()}
    result = 0
    # height = 131
    n = steps_limit // height
    # n = 3
    # even
    result += map_to_points[(0, -1)] * n ** 2
    # odd
    result += map_to_points[(0, 0)] * (n - 1) ** 2
    # corners
    result += map_to_points[(0, -2)] + map_to_points[(2, 0)] + map_to_points[(0, 2)] + map_to_points[(-2, 0)]
    sides = map_to_points[(2, -1)] * (n * 2) + map_to_points[(-1, -2)] * n + map_to_points[(2, 1)] * n
    # 2nd side layer
    n_1 = (map_to_points[(1, -1)] + map_to_points[(-1, -1)] + map_to_points[(1, 1)] + map_to_points[(-1, 1)]) * (n - 1)
    result += n_1 + sides
    print(result)
