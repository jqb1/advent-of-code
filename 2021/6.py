from collections import defaultdict
from copy import copy


def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


print(read_input()[0])


def day_change(lat, r):
    d = defaultdict(int)
    for l_ in lat:
        d[l_] += 1
    for day in range(r):
        zc = 0
        d_next = defaultdict(int)
        for k, v in d.items():
            if k == 0:
                zc += d[k]
            else:
                d_next[k-1] = d[k]
        d_next[6] += zc
        d_next[8] += zc
        d = copy(d_next)
    return d


# each lanternfish creates a new lanternfish once every 7 days
spawn_period = 7

laterns = list(map(int, read_input()[0].split(',')))
laterns_to_add = []
print(laterns)

laterns = day_change(laterns, 256)
print(sum(laterns.values()))