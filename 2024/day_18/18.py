from collections import deque
from heapq import heappop

from utils import read_input, ints

DIRECTION = {
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
}


def solve():
    lines = read_input().split("\n")
    max_r, max_c = 70, 70
    memory = {(row, col): "." for row in range(max_r + 1) for col in range(max_c + 1)}
    for i in range(2500, len(lines)):
        for line in lines[:i]:
            x, y = ints(line)
            memory[y, x] = "#"
        steps = find_path(max_r, max_c, memory)
        if not steps:
            print("ans", lines[i - 1])
            break


def find_path(max_r, max_c, memory):
    start_p, end_p = (0, 0), (max_r, max_c)

    q = [(0, start_p, set())]
    min_steps = None
    lowest_score = {}
    while q:
        steps, (r, c), path = heappop(q)
        if (r, c) == end_p:
            min_steps = steps
            break
        if (r, c) in lowest_score:
            continue
        lowest_score[r, c] = steps
        for dr, dc in DIRECTION:
            if (r + dr, c + dc) in memory and memory[r + dr, c + dc] != "#":
                q.append((steps + 1, (r + dr, c + dc), path | {(r + dr, c + dc)}))
    #
    # for r in range(max_r + 1):
    #     print(["O" if (r, c) in path else memory[r, c] for c in range(max_c + 1)])

    return min_steps


if __name__ == "__main__":
    solve()
