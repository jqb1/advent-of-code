def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


def solve():
    input_ = read_input()
    for line in input_:
        line = line.split("->")
        print(line)
solve()
