from functools import cache

from utils import read_input, submit


def solve():
    stones = list(map(int, read_input()[0].split()))
    res = sum(dfs_stones(stone, 25) for stone in stones)
    submit(res, 2)


def solve_p2():
    stones = list(map(int, read_input()[0].split()))
    res = sum(dfs_stones(stone, 75) for stone in stones)
    submit(res, 2)


@cache
def dfs_stones(stone, steps):
    if steps == 0:
        return 1
    elif stone == 0:
        return dfs_stones(1, steps - 1)
    elif len(str(stone)) % 2 == 0:
        sstone = str(stone)
        lp, rp = int(sstone[: len(sstone) // 2]), int(sstone[len(sstone) // 2 :])
        return sum(dfs_stones(stone, steps - 1) for stone in (lp, rp))
    else:
        return dfs_stones(stone * 2024, steps - 1)


if __name__ == "__main__":
    # solve()
    solve_p2()
