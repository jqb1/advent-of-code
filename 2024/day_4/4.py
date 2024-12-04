from collections import defaultdict

from utils import read_input


def solve_p1():
    grid = defaultdict(str) | {(r, c): l for r, row in enumerate(read_input())
                               for c, l in enumerate(row)}
    xmas = "XMAS"

    pos_d = (0, 1, -1)
    deltas = [(dr, dc) for dr in pos_d for dc in pos_d]

    ans = 0
    gk = list(grid.keys())
    for r, c in gk:
        for dr, dc in deltas:
            w = [grid[r + dr * n, c + dc * n] for n in range(len(xmas))]
            if w == list(xmas):
                ans += 1
    print(ans)


def solve_p2():
    grid = defaultdict(str) | {(r, c): l for r, row in enumerate(read_input())
                               for c, l in enumerate(row)}
    ans = 0
    gk = list(grid.keys())
    pos_w = [list("MAS"), list("SAM")]
    for r, c in gk:
        if grid[r, c] in {"M", "S"}:
            dr, dc = (1, 1)
            w1 = [grid[r + dr * n, c + dc * n] for n in range(3)]
            dr, dc = (1, -1)
            c += 2
            w2 = [grid[r + dr * n, c + dc * n] for n in range(3)]
            if w1 in pos_w and w2 in pos_w:
                ans += 1
    print(ans)


if __name__ == "__main__":
    # solve_p1()
    solve_p2()
