from collections import deque
from operator import add, mul

from utils import read_input


def solve():
    lines = read_input()
    ans = 0
    for line in lines:
        tv, eq = line.split(":")
        tv = int(tv)
        eq = list(map(int, eq.split()))

        pos_values = set()
        q = deque([(0, eq[0])])
        while q:
            ei, cv = q.popleft()
            if cv == tv and ei == len(eq) - 1:
                ans += cv
                break
            pos_values.add(cv)
            # p1 just remove || and if below
            for op in (add, mul, "||"):
                if ei < len(eq) - 1:
                    if op == "||":
                        q.append((ei + 1, int(str(cv) + str(eq[ei + 1]))))
                    else:
                        q.append((ei + 1, op(cv, eq[ei + 1])))
    print(ans)


if __name__ == "__main__":
    solve()
