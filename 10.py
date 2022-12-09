def read_input():
    with open("/Users/jkoziol/Downloads/input.txt") as f:
        moves = [line.rstrip() for line in f]
    return moves


print(read_input())
x1, x2, y1, y2 = 0, 0, 0, 0
lines = [tuple(map(int, line.replace(" -> ", ",").split(','))) for line in read_input()]
print(lines)