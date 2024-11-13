def read_input():
    with open("./input.txt") as f:
        lines = f.read()
    return lines


ORG_RES = {}


def solve():
    input_ = read_input().split("\n\n")
    patterns = [pattern.split("\n") for pattern in input_]
    s = 0
    for pi, pattern in enumerate(patterns):
        cols, rows = find_reflections(pattern)
        ORG_RES[pi] = (cols, rows)
        s += cols + rows
    print("answ", s)

    p2_s = 0
    for pattern_i, pattern in enumerate(patterns):
        cols, rows = find_reflections_p2(pattern, pattern_i)
        p2_s += cols + rows
    print("part2", p2_s)


def find_reflections(pattern):
    cols = list(zip(*pattern))
    for c, col in enumerate(cols):
        if c == len(cols) - 1:
            break
        if check_reflected(c, c + 1, cols):
            left_cols = c + 1
            return left_cols, 0
    for r, row in enumerate(pattern):
        if r == len(pattern) - 1:
            break
        if check_reflected(r, r + 1, pattern):
            above_rows = r + 1
            return 0, above_rows * 100
    return 0, 0


def find_reflections_p2(pattern, pattern_i):
    cols = list(zip(*pattern))
    for c, col in enumerate(cols):
        if c == len(cols) - 1:
            break
        if c + 1 != ORG_RES[pattern_i][0] and check_and_fix(c, c + 1, cols, 0):
            left_cols = c + 1
            return left_cols, 0
    for r, row in enumerate(pattern):
        if r == len(pattern) - 1:
            break
        if (r + 1) * 100 != ORG_RES[pattern_i][1] and check_and_fix(
            r, r + 1, pattern, 0
        ):
            above_rows = r + 1
            return 0, above_rows * 100
    return 0, 0


def check_reflected(first_p, second_p, pattern):
    if first_p < 0 or second_p >= len(pattern):
        return True
    if pattern[first_p] == pattern[second_p]:
        return check_reflected(first_p - 1, second_p + 1, pattern)
    else:
        return False


def check_and_fix(first_p, second_p, pattern, fix_cnt):
    if first_p < 0 or second_p >= len(pattern):
        if fix_cnt == 1:
            return True
        return False
    if fix_cnt > 1:
        return False
    if pattern[first_p] == pattern[second_p]:
        return check_and_fix(first_p - 1, second_p + 1, pattern, fix_cnt)
    elif len(set(enumerate(pattern[first_p])) - set(enumerate(pattern[second_p]))) == 1:
        return check_and_fix(first_p - 1, second_p + 1, pattern, fix_cnt + 1)
    else:
        return False


solve()
