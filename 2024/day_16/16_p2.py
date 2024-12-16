from heapq import heappop, heappush

from utils import read_input

DIRECTION = {
    "l": (0, -1),
    "r": (0, 1),
    "u": (-1, 0),
    "d": (1, 0),
}
TURN = {
    ("r", "r"): "d",
    ("r", "l"): "u",
    ("l", "l"): "d",
    ("l", "r"): "u",
    ("u", "r"): "r",
    ("u", "l"): "l",
    ("d", "l"): "r",
    ("d", "r"): "l",
}


def solve():
    start_p, end_p, grid = None, None, {}
    lines = read_input().split("\n")
    for r, line in enumerate(lines):
        for c, col in enumerate(line):
            grid[r, c] = col
            if col == "E":
                end_p = (r, c)
            elif col == "S":
                start_p = (r, c)

    assert grid[start_p] == "S"

    d = "r"
    q = [(0, start_p, d, set())]
    lowest_score = {}
    best_score = 93436  # copied from the part 1 answer
    best_paths = set()
    while q:
        score, pos, d, path = heappop(q)
        if pos == end_p:
            if score == best_score:
                best_paths |= path
                best_paths |= {end_p}
            continue
        if (pos, d) in lowest_score and score > lowest_score[(pos, d)]:
            continue
        lowest_score[(pos, d)] = score
        r, c = pos
        dr, dc = DIRECTION[d]
        for ct in (d, TURN[d, "r"], TURN[d, "l"]):
            if ct != d:
                heappush(q, (score + 1000, (r, c), ct, path))
            elif (r + dr, c + dc) in grid and grid[r + dr, c + dc] != "#":
                heappush(q, (score + 1, (r + dr, c + dc), ct, path | {pos}))

    print("ans:", len(best_paths))


def print_map(lines, grid, path):
    for r, line in enumerate(lines):
        row = []
        for c, p in enumerate(line):
            if (r, c) in path:
                row.append("O")
            else:
                row.append(grid[r, c])
        print(row)


if __name__ == "__main__":
    solve()
