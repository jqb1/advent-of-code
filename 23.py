import sys
from collections import deque


def read_input():
    with open("/Users/jkoziol/Downloads/input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


DIRECTION = {
    's': (1, 0),
    'n': (-1, 0),
    'w': (0, -1),
    'e': (0, 1),
}

CHECK_DIR = {
    'n': ((-1, 0), (-1, -1), (-1, 1)),
    's': ((1, 0), (1, -1), (1, 1)),
    'w': ((0, -1), (-1, -1), (1, -1)),
    'e': ((0, 1), (-1, 1), (1, 1)),
}


def main(part):
    grove = [list(row) for row in read_input()]
    directions_q = deque(['n', 's', 'w', 'e'])
    elf_positions = {(row, col) for row in range(len(grove)) for col in range(len(grove[0])) if grove[row][col] == "#"}

    for round_ in range(10 if part == 1 else 10000):
        dont_move = set()
        prop_moves = set()

        proposed_positions = {}

        # proposing steps
        for elf_pos in elf_positions:
            neighbor_count = 0
            new_dir = None
            for dir_ in directions_q:
                if check_dir(elf_pos, dir_, elf_positions):
                    new_dir = dir_ if not new_dir else new_dir
                else:
                    neighbor_count += 1
            if new_dir and neighbor_count > 0:
                dr, dc = DIRECTION[new_dir]
                new_pos = (elf_pos[0] + dr, elf_pos[1] + dc)
                if new_pos in prop_moves:
                    dont_move.add(new_pos)
                else:
                    prop_moves.add(new_pos)
                proposed_positions[elf_pos] = new_pos

        # moving step
        new_elf_pos = set()
        c = 0
        for elf_pos in elf_positions:
            new_pos = proposed_positions.get(elf_pos)
            if new_pos and new_pos not in dont_move:
                new_elf_pos.add(new_pos)
                c += 1
            else:
                new_elf_pos.add(elf_pos)
        #  end of the round, the first direction is moved to the end of the list of directions
        if c == 0 and part == 2:
            print(round_ + 1)
            sys.exit(0)
        d = directions_q.popleft()
        directions_q.append(d)
        elf_positions = new_elf_pos

    print(elf_positions)
    min_row_, min_col_ = min(elf_positions, key=lambda x: x[0])[0], min(elf_positions, key=lambda x: x[1])[1]
    max_row_, max_col_ = max(elf_positions, key=lambda x: x[0])[0], max(elf_positions, key=lambda x: x[1])[1]
    display_positions(elf_positions, max_row_, min_row_, max_col_, min_col_)
    print(min_row_, min_col_, max_row_, max_col_)
    print(((max_col_ - min_col_ + 1) * (max_row_ - min_row_ + 1)) - len(elf_positions))


def display_positions(elf_positions, max_row, min_row, max_col, min_col):
    row_num, col_num = abs(max_row - min_row), abs(max_col - min_col)
    grove = [['.'] * (col_num + 1) for _ in range(row_num + 1)]
    for pos in elf_positions:
        grove[pos[0] + abs(min_row)][pos[1] + abs(min_col)] = "#"

    for r in range(len(grove)):
        print(' '.join([grove[r][c] for c in range(len(grove[0]))]))


def check_dir(pos, direction, elf_positions):
    if all((pos[0] + dr, pos[1] + dc) not in elf_positions for dr, dc in CHECK_DIR[direction]):
        return True
    return False


if __name__ == "__main__":
    main(part=1)
    main(part=2)
