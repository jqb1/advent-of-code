def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


def solve():
    input_ = read_input()
    times, distances = input_[0], input_[1]
    # p1
    # times = map(int, times.split()[1:])
    # distances = map(int, distances.split()[1:])
    record_time = int("".join(times.split()[1:]))
    record_dist = int("".join(distances.split()[1:]))
    print(record_time, record_dist)

    explore_possible(record_time, record_dist)


def explore_possible(time_, record_dist):
    speed = 0
    c = 0
    # hold
    for ms in range(1, time_ + 1):
        speed += 1
        res_dist = (time_ - ms) * speed
        if res_dist > record_dist:
            c += 1
    print("result", c)


solve()
