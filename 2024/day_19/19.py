from functools import cache

from utils import read_input


def solve():
    towels, designs = read_input().split("\n\n")
    ans = 0
    c = 0
    towels = tuple(towels.split(", "))
    for des in designs.split("\n"):
        if x := is_pos(des, towels):
            ans += x
            c += 1
    print("p1", c, "p2:", ans)


@cache
def is_pos(design, towels):
    if not design:
        return 1
    return sum(
        [
            is_pos(design[len(tow):], towels)
            for tow in towels
            if design[: len(tow)] == tow
        ]
    )


if __name__ == "__main__":
    solve()
