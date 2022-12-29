from collections import defaultdict


def read_input():
    with open("./input.txt") as f:
        moves = [line.rstrip() for line in f]
    return moves


# print(read_input())
x1, x2, y1, y2 = 0, 0, 0, 0
lines = [tuple(map(int, line.replace(" -> ", ",").split(','))) for line in read_input()]

indices = defaultdict(int)

for line in lines:
    x1, y1, x2, y2 = line
    print(x1, y1, x2, y2)
    if not (x1 == x2) and not (y1 == y2):
        if not abs(x1 - x2) == abs(y1 - y2):
            continue
        else:
            dist = abs(x1 - x2)
            cx, cy = x1, y1
            indices[(cx, cy)] += 1
            for s in range(dist):
                if x1 > x2 and y1 < y2:
                    cx -= 1
                    cy += 1
                    indices[(cx, cy)] += 1
                elif x1 < x2 and y1 < y2:
                    cx += 1
                    cy += 1
                    indices[(cx, cy)] += 1
                elif x1 < x2 and y1 > y2:
                    cx += 1
                    cy -= 1
                    indices[(cx, cy)] += 1
                elif x1 > x2 and y1 > y2:
                    cx -= 1
                    cy -= 1
                    indices[(cx, cy)] += 1
    elif x1 == x2:
        yr = range(y1, y2+1) if y1 < y2 else range(y2, y1+1)
        for y_ in yr:
            indices[(x1, y_)] += 1
    elif y1 == y2:
        xr = range(x1, x2+1) if x1 < x2 else range(x2, x1+1)
        for x_ in xr:
            indices[(x_, y1)] += 1

# print(indices)
# print(len(indices))
# print(len(indices) - len(set(indices)))
print(indices.values())
print(len([i for i in indices.values() if i > 1]))