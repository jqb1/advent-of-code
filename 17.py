import sys
from collections import defaultdict
from itertools import cycle


def read_input():
    with open("/Users/jkoziol/Downloads/input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


WIDTH = 7

shapes = (
    (((0, 2), (0, 3), (0, 4), (0, 5)), 1),  # -
    (((0, 3), (1, 2), (1, 3), (1, 4), (2, 3)), 3),  # +
    (((0, 4), (1, 4), (2, 2), (2, 3), (2, 4)), 3),  # _|
    (((0, 2), (1, 2), (2, 2), (3, 2)), 4),  # |
    (((0, 2), (0, 3), (1, 2), (1, 3)), 2),  # ::
)

MOVES = {
    '>': 1,
    '<': -1,
}

JET_PATTERN = list(read_input()[0])
JET_PATTERN_LEN = len(list(read_input()[0]))


def main():
    chamber = [['-'] * 7]
    move_idx = -1
    seen = defaultdict(tuple)
    cycle_hight = 0

    c = 0
    end = False
    while c < 1000000000000:
        for shape in shapes:
            if c == 1000000000000:
                c = 1000000000000
                break
            chamber, move_idx, c, cycle_ = draw_next(chamber, shape, move_idx, c, seen, 2022)
            if cycle_:
                cycle_hight = cycle_
            print(c)
            c += 1
    for r in range(len(chamber)):
        s = ''
        for col in range(len(chamber[0])):
            s += ' ' + chamber[r][col]
        print(s)
    print('')
    print(len(chamber) - 1 + cycle_hight)
    print(c)


def validated_top(chb):
    # walidating last 10 rows to be sure we
    return tuple(tuple(chb[i]) for i in range(len(chb)) if i < 10)


def draw_next(chamber, shape, move_idx, shape_num, seen, required):
    # for part 2 check cycle
    # cycle occurs between two points if shape lands on the same surface and the jet_pattern is the same

    points, height = shape
    points = set(points)
    init_line = ['.'] * 7

    chmbr = [init_line[:] for _ in range(3 + height)] + chamber
    dh = 0

    # most important part for task2, checking if cycle occurs
    if se := seen.get((validated_top(chamber), shape, move_idx)):
        prev_shape_num, prev_index = se
        height = (len(chamber)) - prev_index
        shapes_between = shape_num - prev_shape_num

        cycles_remaining = (1000000000000 - (shape_num - 1))//shapes_between
        dh = height * cycles_remaining
        dshape = shapes_between * cycles_remaining

        shape_num += dshape
        seen.clear()

    else:
        seen[(validated_top(chamber), shape, move_idx)] = (shape_num, len(chamber))

    shape_moves = True
    while shape_moves:
        move_idx = (move_idx + 1) if not move_idx == JET_PATTERN_LEN - 1 else 0
        mv = JET_PATTERN[move_idx]
        print(mv)
        ch = MOVES[mv]
        if all((0 <= (c + ch) < 7) and chmbr[row][c+ch] != "#" for row, c in points):
            points = {(pr, pc + ch) for pr, pc in points}

        if not any((chmbr[row+1][col] == '#' or chmbr[row+1][col] == '-') for row, col in points):
            points = {(pr+1, pc) for pr, pc in points}
            print("\/")

        else:
            shape_moves = False
            for row, col in points:
                chmbr[row][col] = '#'

        # for r in range(len(chmbr)):
        #     s = ''
        #     for c in range(len(chmbr[0])):
        #         s += "#" if (r, c) in points else chmbr[r][c]
        #     print(s)
        print('')
    highest = 0
    for row in range(len(chmbr)):
        if '#' in chmbr[row]:
            highest = row
            break
    chmbr = chmbr[highest:]
    return chmbr, move_idx, shape_num, dh


if __name__ == "__main__":
    main()