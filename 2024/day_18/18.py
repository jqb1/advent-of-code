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

    def run(last_i):
        memory = {
            (row, col): "." for row in range(max_r + 1) for col in range(max_c + 1)
        }
        for line in lines[: last_i + 1]:
            x, y = ints(line)
            memory[y, x] = "#"
        steps = find_path(max_r, max_c, memory)
        if not steps:
            return False
        return True

    def bin_search(min_i, max_i):
        while min_i < max_i:
            mid = (min_i + max_i) // 2
            if not run(mid):
                max_i = mid
            else:
                min_i = mid + 1
        return min_i

    min_b = bin_search(1024, len(lines) - 1)
    print(min_b)
    print("ans", lines[min_b])


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
    return min_steps


if __name__ == "__main__":
    solve()
