def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


def solve():
    input_ = read_input()
    res = 0
    for line in input_:
        line = [int(v) for v in line.split()[::-1]]
        diff = calc_diffs(line)
        res += diff
    print(res)


def calc_diffs(line):
    diffs = []
    all_zero = True
    if not any(line):
        return 0
    for i in range(1, len(line)):
        diffs.append(line[i] - line[i - 1])
        if diffs[-1] != 0 and all_zero:
            all_zero = False
    return line[-1] + calc_diffs(diffs)


solve()
