from collections import deque
from functools import lru_cache


def read_input():
    with open("/Users/jkoziol/Downloads/input.txt") as f:
        lines = [list(line.rstrip()) for line in f]
    return lines


DIRECTION = {
    'l': (0, -1),
    'r': (0, 1),
    'u': (-1, 0),
    'd': (1, 0),
}

BLIZZARD_DIR = {
    '>': 'r',
    '<': 'l',
    '^': 'u',
    'v': 'd',
}


def main():
    valley_map = read_input()
    # -1 to exclude map frame from calculations (left and upper side)
    start_pos = (-1, valley_map[0].index('.') - 1)
    end_pos = (len(valley_map) - 2, valley_map[len(valley_map) - 1].index('.')-1)

    cur_pos = start_pos
    # -1 to exclude frame
    blizzards = {(r - 1, c - 1, BLIZZARD_DIR[valley_map[r][c]]) for r in range(len(valley_map))
                 for c in range(len(valley_map[0])) if valley_map[r][c] in BLIZZARD_DIR.keys()}

    ans = bfs_valley(valley_map, blizzards, cur_pos, end_pos)
    print(ans)


def bfs_valley(valley_map, blizzards, cur_pos, end_pos):
    seen = set()
    max_row, max_col = len(valley_map) - 2, len(valley_map[0]) - 2

    q = deque([(cur_pos, 0, blizzards)])

    min_to_blizzard = {}
    while q:
        cur_pos, minute, blizzards = q.popleft()
        if (cur_pos, minute) in seen:
            continue
        else:
            seen.add((cur_pos, minute))

        cur_r, cur_c = cur_pos
        # cache blizzard positions as they are always the same at a given time
        if min_to_blizzard.get(minute+1):
            next_blizzards, blizzard_positions = min_to_blizzard[minute+1]
        else:
            next_blizzards, blizzard_positions = next_blizzard_positions(blizzards, max_row, max_col)
            min_to_blizzard[minute+1] = (next_blizzards, blizzard_positions)

        print(cur_pos, minute)

        if (cur_r, cur_c) not in blizzard_positions:
            q.append(((cur_r, cur_c), minute + 1, next_blizzards))
        for dr, dc in DIRECTION.values():
            if (cur_r + dr, cur_c + dc) == end_pos:
                return minute + 1
            if ((cur_r + dr, cur_c + dc) not in blizzard_positions
                    and 0 <= cur_r + dr < max_row and 0 <= cur_c + dc < max_col):
                q.append(((cur_r + dr, cur_c + dc), minute + 1, next_blizzards))


def next_blizzard_positions(blizzards, max_row, max_col):
    next_blizzards, blizzard_positions = set(), set()
    for row, col, dir_ in blizzards:
        next_blizzards.add(((row + DIRECTION[dir_][0]) % max_row, (col + DIRECTION[dir_][1]) % max_col, dir_))
        blizzard_positions.add(((row + DIRECTION[dir_][0]) % max_row, (col + DIRECTION[dir_][1]) % max_col))
    return next_blizzards, blizzard_positions


if __name__ == "__main__":
    main()
