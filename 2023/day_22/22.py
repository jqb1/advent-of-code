from collections import defaultdict


def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


def solve():
    inp = read_input()
    bricks = parse_input(inp)
    bricks = sorted(bricks, key=lambda l: l[0][2])

    height_map = defaultdict(int)
    tower = []
    for brick in bricks:
        new_brick, changed = set_brick(brick, height_map)
        tower.append(new_brick)
    c = 0
    for i in range(len(tower)):
        new_height_map = defaultdict(int)
        safe = True
        for brick in tower[:i] + tower[i + 1:]:
            *_, changed = set_brick(brick, new_height_map)
            # part 1
            # if changed:
            #     safe = False
            #     break
            # part 2
            if changed:
                c += 1
    print(c)


def set_brick(brick, height_map):
    (x1, y1, h1), (x2, y2, h2) = brick
    cur_h, new_h, changed = move_down(brick, height_map)
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            height_map[(x, y)] = new_h
    return ((x1, y1, cur_h), (x2, y2, new_h)), changed


def move_down(brick, height_map):
    (x1, y1, h1), (x2, y2, h2) = brick
    cur_h = max(height_map[(x, y)] for y in range(y1, y2 + 1) for x in range(x1, x2 + 1)) + 1
    changed = cur_h != h1
    return cur_h, cur_h + h2 - h1, changed


def parse_input(inp):
    out = []
    for line in inp:
        start, end = line.split("~")
        out.append((tuple(map(int, start.split(","))), tuple(map(int, end.split(",")))))
    return out


solve()
