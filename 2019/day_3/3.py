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
    line1 = line1.split(",")
    line2 = line2.split(",")

    points_l1 = set()



solution = solve()
print(solution)
