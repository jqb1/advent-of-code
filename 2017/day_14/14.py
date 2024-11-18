from collections import deque
from functools import reduce


def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


ROW_N, COL_N = 128, 128


def solve():
    grid = []
    for i in range(ROW_N):
        inp = read_input()[0]
        knot = knot_hash(inp + f"-{i}")
        hash_ = "".join([f"{int(num, 16):04b}" for num in knot])
        grid.append(list(hash_))
    print(grid)
    in_group = set()
    gc = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "1" and (row, col) not in in_group:
                bfs_grid(row, col, in_group, grid)
                gc += 1
    print(gc)


def bfs_grid(row, col, in_group, grid):
    """mutates in_group"""
    delta = {(0, 1), (1, 0), (-1, 0), (0, -1)}
    q = deque([(row, col)])
    while q:
        row, col = q.popleft()
        if (row, col) in in_group:
            continue
        in_group.add((row, col))
        for dr, dc in delta:
            if (
                0 <= row + dr < ROW_N
                and 0 <= col + dc < COL_N
                and grid[row + dr][col + dc] == "1"
            ):
                q.append((row + dr, col + dc))


def knot_hash(input_):
    """copy from day 10"""
    lengths = list(map(ord, input_)) + [17, 31, 73, 47, 23]
    lsize = 256
    hash_out = [i for i in range(lsize)]
    cur_pos = 0
    skip_size = 0
    for i in range(64):
        for l in lengths:
            sub_list = (
                hash_out[cur_pos : cur_pos + l]
                if cur_pos + l < lsize
                else hash_out[cur_pos:] + hash_out[: (cur_pos + l) % lsize]
            )
            sub_list = sub_list[::-1]
            for s_i in range(len(sub_list)):
                hash_out[(cur_pos + s_i) % lsize] = sub_list[s_i]
            cur_pos += l + skip_size
            cur_pos = cur_pos % lsize
            skip_size += 1
    res = []
    for xi in range(0, 256, 16):
        cur_res = reduce(lambda x, y: x ^ y, hash_out[xi : xi + 16])
        res.append(cur_res)
    res = "".join([f"{r:02x}" for r in res])
    return res


solve()
