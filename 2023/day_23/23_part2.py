import sys
from collections import deque, defaultdict


def read_input():
    with open("./input.txt") as f:
        lines = [[ch for ch in line.rstrip()] for line in f]
    return lines


DIRECTIONS = {
    '<': (0, -1),
    '>': (0, 1),
    '^': (-1, 0),
    'v': (1, 0),
}


def solve():
    map_ = read_input()
    start_p = (0, 1)
    max_row = len(map_) - 1
    max_col = len(map_[0]) - 1
    end_p = (max_row, max_col - 1)
    crossings = find_crossings(grid=map_)
    crossings.update({start_p, end_p})

    cr_distances = {}
    for crossing in crossings:
        distances = bfs_distances(crossing, crossings, map_)
        cr_distances[crossing] = distances

    # point, steps, path
    longest = dfs_longest(start_p, 0, end_p, cr_distances, set())
    print(f"longest path {longest}")


CACHE = {}


def bfs_distances(cr, crossings, grid):
    max_row, max_col = len(grid) - 1, len(grid[0]) - 1
    q = deque([(cr, 0, set())])
    seen = set()
    distances = {}
    while q:
        node, steps, path = q.popleft()
        if node in seen:
            continue
        if node in crossings and node != cr:
            distances[node] = steps
            continue
        for dr, dc in DIRECTIONS.values():
            if 0 <= (new_r := node[0] + dr) <= max_row and 0 <= (new_c := node[1] + dc) <= max_col:
                if (new_r, new_c) not in path and grid[new_r][new_c] != "#":
                    q.append(((new_r, new_c), steps + 1, path | {(node[0], node[1])}))
    return distances


def find_crossings(grid):
    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1
    crossings = set()

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "#":
                continue
            paths_c = 0
            for dr, dc in DIRECTIONS.values():
                nr = row + dr
                nc = col + dc
                if nr > max_row or nr < 0 or nc > max_col or nc < 0 or grid[nr][nc] == "#":
                    continue
                paths_c += 1
            if paths_c > 2:
                crossings.add((row, col))
    return crossings


def dfs_longest(node, steps, end_p, crossings, path):
    if node == end_p:
        return steps
    max_dist = 0
    for neighbor, dist in crossings[node].items():
        if neighbor in path:
            continue
        dst = dfs_longest(neighbor, steps+dist, end_p, crossings, path | {node})
        max_dist = max(dst, max_dist)
    return max_dist

solve()
