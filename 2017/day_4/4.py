def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


def solve():
    input_ = read_input()
    s = 0
    for line in input_:
        p = set()
        d = []
        valid = True
        for w in line.split():
            sw = set(w)
            if sw in d:
                valid = False
                break
            d.append(set(w))
        if valid:
            s += 1

    print(s)


solve()
