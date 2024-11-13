def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


DIRECTIONS = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
}

CODE_TO_DIR = {
    "0": "R",
    "1": "D",
    "2": "L",
    "3": "U",
}


def solve():
    inp = read_input()
    x, y = 0, 0
    points = [(x, y)]
    bounds_sum = 0
    for line in inp:
        # part1
        dir_, steps, hex_code = line.split()
        steps = int(steps)

        # part2
        hex_code = hex_code[1:-1]
        dir_ = CODE_TO_DIR[hex_code[-1]]
        steps = int(hex_code[1:-1], 16)
        bounds_sum += steps

        dx, dy = DIRECTIONS[dir_]
        x += dx * steps
        y += dy * steps
        points.append((x, y))

    area_inside = shoelace(points)
    # Pick's theorem, find i + b
    # i -> interior points, b -> boundary points
    # A = i + b/2 -1 => i = A - b/2 + 1 => i + b = A + b/2 + 1
    print(area_inside + bounds_sum // 2 + 1)


def shoelace(points):
    s = 0
    # shoelace formula
    for i in range(len(points) - 1):
        (x1, y1), (x2, y2) = points[i], points[i + 1]
        s += x1 * y2 - x2 * y1
    return abs(s) // 2


solve()
