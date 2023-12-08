import math
from itertools import cycle


def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


def solve():
    input_ = read_input()
    graph = {}
    instructions = cycle(input_[0])
    # part 2
    current_nodes = []

    for line in input_[2:]:
        line = line.split()
        cur, left, right = line[0], line[2][1:-1], line[3][:-1]
        if cur[-1] == "A":
            current_nodes.append(cur)
        graph[cur] = (left, right)

    steps = 0
    node_c = len(current_nodes)
    z_nodes_intervals = {}
    while True:
        lr = next(instructions)
        end_nodes_c = 0
        next_nodes = []
        if lr == "R":
            next_i = 1
        else:
            next_i = 0
        for i, cur_ in enumerate(current_nodes):
            if cur_[-1] == "Z" and not z_nodes_intervals.get(i):
                z_nodes_intervals[i] = steps
                if len(z_nodes_intervals) == node_c:
                    return common_multiplier(z_nodes_intervals)
                end_nodes_c += 1
            next_ = graph[cur_][next_i]
            next_nodes.append(next_)
        steps += 1
        current_nodes = next_nodes


def common_multiplier(intervals):
    return math.lcm(*intervals.values())


print(solve())
