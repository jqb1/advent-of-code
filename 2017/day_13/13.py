def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip().split(": ") for line in f]
    return lines


def solve():
    inp = read_input()
    scan_interval = {}
    for line in inp:
        pos, depth = map(int, line)
        # interval at which scanner will be at position 1
        scan_interval[pos] = (depth - 1) * 2
    last_step = int(inp[-1][0])

    step = 0
    caught = True
    delay = 0
    while caught:  # part2
        caught = False
        while step <= last_step:
            if step in scan_interval and (step + delay) % scan_interval[step] == 0:
                caught = True
                step = 0
                delay += 1
                break
            step += 1
    print(delay)
    # part 1
    # severity = 0
    # for p in caught:
    #     severity += p * scan_state[p][1]
    # print(severity)


solve()
