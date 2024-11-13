def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


def solve():
    x, y = 0, 0
    direction = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, 1),
        "D": (0, -1),
    }
    line1, line2 = read_input()
    line1, line2 = line1.split(","), line2.split(",")

    l1_points = []
    l2_points = []
    for moves in line1:
        dir_, steps = moves[0], int(moves[1:])
        dx, dy = direction[dir_]
        for _ in range(steps):
            x += dx
            y += dy
            l1_points.append((x, y))
    x, y = 0, 0
    for moves in line2:
        dir_, steps = moves[0], int(moves[1:])
        dx, dy = direction[dir_]
        for _ in range(steps):
            x += dx
            y += dy
            l2_points.append((x, y))

    crossings = set(l1_points).intersection(set(l2_points))
    print(crossings)
    p = next(iter(crossings))
    lowest_steps = l1_points.index(p) + 1 + l2_points.index(p) + 1
    for cross in crossings:
        lowest_steps = min(
            lowest_steps, l1_points.index(cross) + 1 + l2_points.index(cross) + 1
        )
    return lowest_steps


solution = solve()
print(solution)
