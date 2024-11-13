def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


def solve():
    input_ = read_input()
    instructions = [int(x) for x in input_]

    max_i = len(instructions) - 1
    cur_i = 0
    steps = 0
    while 0 <= cur_i <= max_i:
        cur = instructions[cur_i]
        next_j = instructions[cur_i]
        if next_j >= 3:
            instructions[cur_i] = cur - 1
        else:
            instructions[cur_i] = cur + 1
        cur_i = cur_i + next_j
        steps += 1
    print(steps)


solve()
