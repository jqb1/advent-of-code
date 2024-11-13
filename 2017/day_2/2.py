def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip().split() for line in f]
    return lines


def solve():
    input_ = read_input()
    s = 0
    for row in input_:
        for i in range(len(row)):
            for j in range(len(row)):
                div, mod = divmod(int(row[i]), int(row[j]))
                if mod == 0 and i != j:
                    print(div, mod)
                    s += div
    print(s)


solve()
