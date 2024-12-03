from collections import defaultdict

from utils import read_input, submit

DIRECTION = {
    "l": (0, -1),
    "r": (0, 1),
    "u": (-1, 0),
    "d": (1, 0),
}

TURN = {
    ("r", "r"): "d",
    ("r", "rev"): "l",
    ("r", "l"): "u",
    ("l", "l"): "d",
    ("l", "r"): "u",
    ("l", "rev"): "r",
    ("u", "r"): "r",
    ("u", "l"): "l",
    ("u", "rev"): "d",
    ("d", "l"): "r",
    ("d", "r"): "l",
    ("d", "rev"): "u",
}

NEW_STATE = {
    ".": "W",
    "W": "#",
    "#": "F",
    "F": ".",
}


def solve():
    lines = read_input()
    grid = defaultdict(lambda: ".")
    cur_p = ("u", len(lines) // 2, len(lines[0]) // 2)
    for cr, row in enumerate(lines):
        for cc, _ in enumerate(row):
            grid[(cr, cc)] = lines[cr][cc]
    print(grid)
    ans = 0
    d, r, c = cur_p
    for i in range(10000000):
        cur_n = grid[(r, c)]
        d = d_change(d, cur_n)
        if cur_n == ".":
            grid[(r, c)] = "W"
        elif cur_n == "W":
            grid[(r, c)] = "#"
            ans += 1
        elif cur_n == "#":
            grid[(r, c)] = "F"
        elif cur_n == "F":
            grid[(r, c)] = "."
        dr, dc = DIRECTION[d]
        r += dr
        c += dc

    submit(ans, 2)


def d_change(d, node):
    match node:
        case ".":
            return TURN[(d, "l")]
        case "#":
            return TURN[(d, "r")]
        case "W":
            return d
        case "F":
            return TURN[(d, "rev")]


if __name__ == "__main__":
    solve()
