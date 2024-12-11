from utils import read_input, submit


def solve():
    lines = read_input().split('\n')
    grid = {}
    antennas = {}
    antinodes = set()
    for r, line in enumerate(lines):
        for c, v in enumerate(list(line)):
            grid[r, c] = v
            if v.isalnum():
                antennas[r, c] = v

    for r1, c1 in antennas:
        for r2, c2 in antennas:
            if (r1, c1) == (r2, c2):
                continue
            # same freq
            if antennas[r1, c1] == antennas[r2, c2]:
                dr, dc = dist((r1, c1), (r2, c2))
                if (ant := (r1 + dr * 2, c1 + dc * 2)) in grid:
                    antinodes.add(ant)
    print_map(lines, antinodes)
    submit(len(antinodes), 1)


def dist(a, b):
    return b[0] - a[0], b[1] - a[1]


def print_map(grid, antinodes):
    for r, row in enumerate(grid):
        c = ["#" if (r, col) in antinodes else grid[r][col] for col in range(len(row))]
        print(c)
    print()


def solve_p2():
    lines = read_input().split('\n')
    grid = {}
    antennas = {}
    antinodes = set()
    for r, line in enumerate(lines):
        for c, v in enumerate(list(line)):
            grid[r, c] = v
            if v.isalnum():
                antennas[r, c] = v

    for r1, c1 in antennas:
        for r2, c2 in antennas:
            if (r1, c1) == (r2, c2):
                continue
            # same freq
            if antennas[r1, c1] == antennas[r2, c2]:
                dr, dc = dist((r1, c1), (r2, c2))
                nr, nc = r1, c1
                while True:
                    nr += dr
                    nc += dc
                    if (nr, nc) in grid:
                        antinodes.add((nr, nc))
                    else:
                        break
    submit(len(antinodes), 2)


if __name__ == "__main__":
    solve()
