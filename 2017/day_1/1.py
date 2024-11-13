def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip().split(":") for line in f]
    return lines


def solve():
    input_ = read_input()[0][0]
    s = 0
    steps = len(input_) / 2
    for i, d in enumerate(input_):
        n = int((i + steps) % len(input_))
        if d == input_[n]:
            s += int(d)
    print(s)


solve()
