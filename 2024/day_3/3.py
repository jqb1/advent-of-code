import re
from collections import defaultdict, deque

from utils import read_input, submit


def solve():
    lines = read_input()
    ans = 0
    can_mul = True
    for line in lines:
        muls = list(re.finditer(r"mul\((-?\d+),(-?\d+)\)|do\(\)|don\'t\(\)", line))
        for mu in muls:
            if mu.group() == "don't()":
                can_mul = False
                continue
            elif mu.group() == "do()":
                can_mul = True
            else:
                mu = mu.groups()
                if can_mul:
                    ans += int(mu[0]) * int(mu[1])
    submit(ans, 2)


if __name__ == "__main__":
    solve()
