def read_input():
    with open("./input.txt") as f:
        lines = [int(line.rstrip()) for line in f]
    return lines


def solve():
    input_ = read_input()
    fuel = [calc_fuel(n) for n in input_]
    return sum(fuel)

def calc_fuel(f):
    s = 0
    while f >= 0:
        f = (f // 3) - 2
        if f >= 0:
            s += f
    return s


solution = solve()
print(solution)
#
# solution = calc_fuel(100756)
# print(solution)