from functools import cache


def read_input():
    with open("./input.txt") as f:
        lines = [line for line in f]
    return lines


CACHE = {}
ROW = []
CRITERIA = []


def solve():
    input_ = read_input()
    res = 0
    for springs in input_:
        row, criteria = springs.split()
        # p2
        row = "?".join(row for _ in range(5))
        for el in row:
            ROW.append(el)
        criteria = ",".join(criteria for _ in range(5))
        criteria = [int(c) for c in criteria.split(",")]
        for c in criteria:
            CRITERIA.append(c)
        c_r = find_permutations(0, 0, 0)
        print(c_r)
        find_permutations.cache_clear()
        ROW.clear()
        CRITERIA.clear()
        res += c_r
    print(res)


@cache
def find_permutations(current_i, group_i, damaged_cnt):
    row = ROW
    criteria = CRITERIA
    if current_i >= len(row):
        if group_i >= len(criteria) and not damaged_cnt:
            return 1
        if group_i == len(criteria) - 1 and damaged_cnt == criteria[group_i]:
            return 1
        return 0
    cur_springs = [".", "#"] if row[current_i] == "?" else [row[current_i]]
    res = 0
    for spring in cur_springs:
        if spring == "." and group_i < len(criteria) and criteria[group_i] == damaged_cnt:
            res += find_permutations(current_i + 1, group_i + 1, 0)
        elif spring == "." and damaged_cnt == 0:
            res += find_permutations(current_i + 1, group_i, 0)
        elif spring == "#" and group_i < len(criteria) and damaged_cnt < criteria[group_i]:
            res += find_permutations(current_i + 1, group_i, damaged_cnt + 1)
    return res


solve()
