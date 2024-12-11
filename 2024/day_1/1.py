from collections import defaultdict

from utils import read_input, submit


def solve():
    lines = read_input().split('\n')
    print(lines)
    l1 = []
    l2 = defaultdict(int)
    for line in lines:
        n1, n2 = line.split()
        l1.append(n1)
        l2[n2] += 1
    l1 = sorted(l1)
    ans = 0
    for n1 in l1:
        ans += abs(l2[n1] * int(n1))
    print(ans)
    submit(ans, 2)


if __name__ == "__main__":
    solve()
