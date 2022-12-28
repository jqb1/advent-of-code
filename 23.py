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


def main():
    grove = [['.'] * 150 for _ in range(150)]

    grove_in = [list(row) for row in read_input()]
    for r in range(len(grove_in)):
        for c in range(len(grove_in[0])):
            grove[r+50][c+50] = grove_in[r][c]

    directions_q = deque(['n', 's', 'w', 'e'])

    for _ in range(10):
        dont_move = set()
        prop_moves = set()

        new_positions = {}

        elf_positions = {(row, col) for row in range(len(grove)) for col in range(len(grove[0])) if grove[row][col] == "#"}

        # proposing steps
        for elf_pos in elf_positions:
            neighbor_count = 0
            new_dir = None
            for dir_ in directions_q:
                if check_dir(elf_pos, dir_, elf_positions):
                    dr, dc = DIRECTION[dir_]
                    # needs to be removed, instead extend the grove
                    # if elf_pos[0] + dr < 0 or elf_pos[0] + dr >= max_row or elf_pos[1] + dc >= max_col or elf_pos[1] + dc < 0:
                    #     continue
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
                new_positions[elf_pos] = new_pos

        # moving step
        r_inserted, c_inserted = 0, 0
        for elf_pos in elf_positions:
            new_pos = new_positions.get(elf_pos)
            if new_pos and new_pos not in dont_move:
                # if new_pos[0] < 0 or new_pos[0] >= len(grove) or new_pos[1] >= len(grove[0]) or new_pos[1] < 0:
                #     dr, dc = extend_grove(new_pos, grove, r_inserted, c_inserted)
                #     r_inserted += dr
                #     c_inserted += dc
                # new_pos_r = new_pos[0] + (r_inserted if new_pos[0] < len(grove)-1 else 0)
                # new_pos_c = new_pos[1] + (c_inserted if new_pos[1] < len(grove[0])-1 else 0)
                # grove[new_pos_r][new_pos_c] = "#"
                # grove[elf_pos[0]+r_inserted][elf_pos[1]+c_inserted] = "."
                grove[new_pos[0]][new_pos[1]] = "#"
                grove[elf_pos[0]][elf_pos[1]] = "."
        #  end of the round, the first direction is moved to the end of the list of directions
        d = directions_q.popleft()
        directions_q.append(d)

    elf_positions = {(row, col) for row in range(len(grove)) for col in range(len(grove[0])) if grove[row][col] == "#"}

    for r in grove:
        print(' '.join([c for c in r]))
    print(elf_positions)
    min_row_, min_col_ = min(elf_positions, key=lambda x: x[0])[0], min(elf_positions, key=lambda x: x[1])[1]
    max_row_, max_col_ = max(elf_positions, key=lambda x: x[0])[0], max(elf_positions, key=lambda x: x[1])[1]
    print(min_row_, min_col_, max_row_, max_col_)
    print(((max_col_-min_col_+1) * (max_row_ - min_row_+1)) - len(elf_positions))


def extend_grove(position, grove, r_inserted, c_inserted):
    row, col = position
    if row >= len(grove):
        grove.append(['.'] * len(grove[0]))
        return 0, 0
    elif col >= len(grove[0]):
        for row in grove:
            row.append('.')
        return 0, 0
    elif col < 0 and c_inserted == 0:
        for row in grove:
            row.insert(0, '.')
        return 0, 1
    elif row < 0 and r_inserted == 0:
        grove.insert(0, ['.'] * len(grove[0]))
        return 1, 0
    return 0, 0


def check_dir(pos, direction, elf_positions):
    if all((pos[0]+dr, pos[1] + dc) not in elf_positions for dr, dc in CHECK_DIR[direction]):
        return True
    return False


if __name__ == "__main__":
    main()
