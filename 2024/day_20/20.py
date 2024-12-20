from collections import deque

from utils import read_input

DIRECTIONS = (
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
)

MIN_SAVED = 100
STEPS = 20


def solve():
    lines = read_input().split("\n")
    grid = {}
    start_p, end_p = None, None
    for r, row in enumerate(lines[1:-1]):
        for c, el in enumerate(row[1:-1]):
            if el == "S":
                start_p = (r, c)
            elif el == "E":
                end_p = (r, c)
            grid[r, c] = el
    assert grid[start_p] == "S"
    assert grid[end_p] == "E"

    first_path_l, original_path = explore(grid, start_p, end_p, 10000, False, 10000)
    print("first path", first_path_l)
    ans = set()
    c = 0
    for pos in original_path:
        cheats = explore_cheats(pos, original_path)
        for e, steps in cheats.items():
            if (pos, e) in ans:
                continue
            diff = original_path[e] - steps - original_path[pos]
            if diff >= MIN_SAVED:
                c += 1
            ans.add((pos, e))
    print("ans", c)


def explore_cheats(start_p, orig_path):
    e_to_steps = {}
    for p, orig_ps in orig_path.items():
        diff = orig_path[p] - orig_path[start_p]
        dist = abs(start_p[0] - p[0]) + abs(start_p[1] - p[1])
        if diff >= MIN_SAVED and dist <= STEPS:
            e_to_steps[p] = dist
    return e_to_steps


def explore(grid, start_p, end_p, max_ps, cheat, diff):
    q = deque([(0, start_p)])
    path = {}
    while q:
        picos, p = q.popleft()
        if picos >= diff:
            continue
        if p in path:
            continue
        path[p] = picos
        if p == end_p:
            return picos, path
        if picos == max_ps:
            continue

        r, c = p
        for dr, dc in DIRECTIONS:
            if (pp := (r + dr, c + dc)) in grid and (grid[pp] != "#" or cheat):
                if pp not in path:
                    q.append((picos + 1, pp))


if __name__ == "__main__":
    solve()
