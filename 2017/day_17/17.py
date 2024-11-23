def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


def solve():
    steps = int(read_input()[0])
    insert_n = 50000000
    insert_c = 1
    cur_val = 0
    cur_i = 0
    buffer = [cur_val]

    # p2
    after_0 = None
    while insert_c <= insert_n:
        cur_val += 1
        cur_i = (cur_i + steps) % insert_c
        if cur_i == 0:
            after_0 = cur_val
        # part1
        # buffer = buffer[:cur_i+1] + [cur_val] + buffer[cur_i+1:]
        cur_i += 1
        insert_c += 1
        if insert_c % 1000 == 0:
            print(f"step: {insert_c}")
    # p1
    # print(buffer[cur_i+1])
    # p2
    print(after_0)


solve()
