from utils import read_input, submit
from collections import deque, defaultdict

DIRECTION = {
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
}


def solve():
    lines = read_input().split("\n")
    ans = 0
    grid = {}
    trailheads = []
    for r, line in enumerate(lines):
        for c, num in enumerate(line):
            if num == ".":
                continue
            num = int(num)
            grid[r, c] = num
            if num == 0:
                cur_p = (r, c)
                trailheads.append(cur_p)
    for th in trailheads:
        q = deque([th])
        seen = set()
        score = 0
        while q:
            cur_p = q.popleft()
            height = grid[cur_p]
            if cur_p in seen:
                continue
            seen.add(cur_p)
            if height == 9:
                score += 1
                continue
            for dr, dc in DIRECTION:
                r, c = cur_p
                if (r + dr, c + dc) in grid and grid[r + dr, c + dc] == height + 1:
                    q.append((r + dr, c + dc))

        print(th, score)
        ans += score
    submit(ans, 1)


def solve_p2():
    lines = read_input().split("\n")
    ans = 0
    grid = {}
    trailheads = []
    for r, line in enumerate(lines):
        for c, num in enumerate(line):
            if num == ".":
                continue
            num = int(num)
            grid[r, c] = num
            if num == 0:
                cur_p = (r, c)
                trailheads.append(cur_p)
    for th in trailheads:
        q = deque([(th, str(th))])
        paths = set()
        seen = set()
        while q:
            cur_p, path = q.popleft()
            height = grid[cur_p]
            if path in seen:
                continue
            seen.add(path)
            if height == 9:
                paths.add(path)
                continue
            for dr, dc in DIRECTION:
                r, c = cur_p
                if (r + dr, c + dc) in grid and grid[r + dr, c + dc] == height + 1:
                    q.append(((r + dr, c + dc), path + str((r + dr, c + dc))))

        print(th, paths)
        ans += len(paths)
    submit(ans, 2)


if __name__ == "__main__":
    # solve()
    solve_p2()
