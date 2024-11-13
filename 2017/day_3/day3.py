from itertools import cycle


def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip().split() for line in f]
    return lines


def solve():
    end_square = read_input()[0][0]
    num = find_end_square(int(end_square))
    # dist = abs(end_x) + abs(end_y)
    print(num)


def find_end_square(end_square):
    directions = cycle([(0, 1), (-1, 0), (0, -1), (1, 0)])
    x, y = 0, 0

    sq_num = 1
    direction = (1, 0)
    steps = 0
    point_to_val = {(0, 0): 1}
    adjacent_list = [
        (-1, 1),
        (0, 1),
        (1, 1),
        (-1, 0),
        (1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
    ]

    while sq_num < int(end_square):
        if direction == (1, 0):  # if previous was right, increase by 1 to right,
            x += 1
            steps += 2
            sq_num = sum(
                point_to_val.get((x + adj_x, y + adj_y), 0)
                for adj_x, adj_y in adjacent_list
            )
            point_to_val[(x, y)] = sq_num
        direction = next(directions)
        dx, dy = direction
        for _ in range(steps - 1 if direction == (0, 1) else steps):
            # if sq_num == end_square:
            #     return x, y
            x += dx
            y += dy
            # part 1
            # sq_num += 1
            # part 2
            sq_num = sum(
                point_to_val.get((x + adj_x, y + adj_y), 0)
                for adj_x, adj_y in adjacent_list
            )
            print(sq_num)
            point_to_val[(x, y)] = sq_num
            if sq_num > end_square:
                return sq_num


solve()
