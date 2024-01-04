from collections import deque


def read_input():
    with open("./input_t.txt") as f:
        lines = [[ch for ch in line.rstrip()] for line in f]
    return lines


DIRECTIONS = {
    '<': (0, -1),
    '>': (0, 1),
    '^': (-1, 0),
    'v': (1, 0),
}


def solve():
    map_ = read_input()
    start_p = (0, 1)
    max_row = len(map_) - 1
    max_col = len(map_[0]) - 1
    end_p = (max_row, max_col - 1)

    # point, steps, path
    q = deque([(start_p, 0, set())])
    seen = set()
    longest_path = 0
    while q:
        (pr, pc), steps, path = q.popleft()
        if (pr, pc, steps) in seen or (pr, pc) in path:
            continue
        seen.add((pr, pc, steps))
        if (pr, pc) == end_p:
            longest_path = max(longest_path, steps)
            print(longest_path, len(q))
            continue
        tile = map_[pr][pc]
        if tile in DIRECTIONS:
            dr, dc = DIRECTIONS[tile]
            q.append(((pr+dr, pc+dc), steps + 1, path | {(pr, pc)}))
        else:
            for dr, dc in DIRECTIONS.values():
                if 0 <= (new_r := pr + dr) <= max_row and 0 <= (new_c := pc + dc) <= max_col and map_[new_r][new_c] != "#":
                    # if not (new_r, new_c) in path:
                    q.append(((new_r, new_c), steps + 1, path | {(pr, pc)}))

    print(f"longest path {longest_path}")


solve()
