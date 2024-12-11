from utils import read_input

DIRECTION = {
    "l": (0, -1),
    "r": (0, 1),
    "u": (-1, 0),
    "d": (1, 0),
}

TURN = {
    # d = current direction
    # (d, turn): (result)
    ("r", "r"): "d",
    ("r", "l"): "u",
    ("l", "l"): "d",
    ("l", "r"): "u",
    ("u", "r"): "r",
    ("u", "l"): "l",
    ("d", "l"): "r",
    ("d", "r"): "l",
}


def solve_p1_p2():
    grid = {}
    lines = read_input().split('\n')
    start_p = None
    for r, row in enumerate(lines):
        for c, col in enumerate(list(row)):
            if lines[r][c] == "^":
                start_p = r, c
            grid[r, c] = lines[r][c]
    d = "u"
    seen, _ = simulate_path(grid, start_p, d, None)
    print("p1", len({p[0:2] for p in seen}))
    seen -= {start_p}
    obstacles = set()
    for pos_obstacle in seen:
        obs = pos_obstacle[0], pos_obstacle[1]
        _, cycle = simulate_path(grid, start_p, d, obs)
        if cycle:
            obstacles.add(obs)
    print("p2", len(obstacles))


def simulate_path(grid, start_p, d, obstacle):
    cur_p = start_p
    seen = set()
    cycle = False
    while True:
        dr, dc = DIRECTION[d]
        r, c = cur_p
        if cur_p not in grid:
            break
        seen.add((r, c, d))
        if (r + dr, c + dc) in grid and (
            grid[r + dr, c + dc] == "#" or (r + dr, c + dc) == obstacle
        ):
            d = TURN[d, "r"]
            dr, dc = DIRECTION[d]
            if (r + dr, c + dc, d) in seen:
                # cycle found
                return seen, True
        cur_p = (r + dr, c + dc)
    return seen, cycle


if __name__ == "__main__":
    solve_p1_p2()
