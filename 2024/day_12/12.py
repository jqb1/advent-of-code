from utils import read_input, submit
from collections import defaultdict, deque

DIRECTION = {
    "l": (0, -1),
    "r": (0, 1),
    "u": (-1, 0),
    "d": (1, 0),
}


def solve():
    lines = read_input().split("\n")
    ans = 0
    grid = {}
    seen = set()
    for r, row in enumerate(lines):
        for c, letter in enumerate(row):
            grid[r, c] = letter
    for r, c in grid:
        if (r, c) in seen:
            continue
        perim, area = explore_area((r, c), grid, seen)
        ans += perim * area
    submit(ans, 1)


def explore_area(cur_p, grid, seen):
    total_perim = 0
    area = 0
    q = deque([cur_p])
    reg_id = grid[cur_p]
    while q:
        (r, c) = q.popleft()
        if (r, c) in seen:
            continue
        area += 1
        total_perim += 4
        seen.add((r, c))
        for dr, dc in DIRECTION.values():
            pp = (r + dr, c + dc)
            if pp in grid and grid[pp] == reg_id:
                total_perim -= 1
                q.append(pp)
    return total_perim, area


# ========== p2 ==========


def solve_p2():
    lines = read_input().split("\n")
    ans = 0
    grid = {}
    seen = set()
    for r, row in enumerate(lines):
        for c, letter in enumerate(row):
            grid[r, c] = letter
    for r, c in grid:
        if (r, c) in seen:
            continue
        sides, area = explore_area_2((r, c), grid, seen)
        ans += sides * area
    submit(ans, 2)


def explore_area_2(cur_p, grid, seen):
    area = 0
    q = deque([cur_p])
    reg_id = grid[cur_p]
    fence = {}
    sides = 0
    while q:
        (r, c) = q.popleft()
        if (r, c) in seen:
            continue
        area += 1
        seen.add((r, c))
        for d, (dr, dc) in DIRECTION.items():
            pp = (r + dr, c + dc)
            if pp in grid and grid[pp] == reg_id:
                q.append(pp)
            # if no neighbor, check if new side
            else:
                axis = "row" if dr != 0 else "col"
                if check_new_side(pp, fence, axis, d):
                    sides += 1
                fence[pp, d, axis] = reg_id
    return sides, area


def check_new_side(pp, fence, axis, d):
    r, c = pp
    if axis == "row":
        # left
        if ((r, c - 1), d, axis) in fence:
            return False
        # right
        elif ((r, c + 1), d, axis) in fence:
            return False
        return True
    else:
        # down
        if ((r - 1, c), d, axis) in fence:
            return False
        # up
        elif ((r + 1, c), d, axis) in fence:
            return False
        return True


if __name__ == "__main__":
    # solve()
    solve_p2()
