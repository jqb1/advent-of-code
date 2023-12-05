def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


def solve():
    #p1
    input_ = read_input()
    # seeds = map(int, input_[0].split()[1:])
    # p2
    start = None
    seeds = []
    for seed in map(int, input_[0].split()[1:]):
        if start:
            end = start + seed
            seeds.extend(range(start, end))
            start = None
        else:
            start = seed

    id_to_new = dict.fromkeys(seeds)
    print(input_)
    for line in input_[3:]:
        if not line:
            continue
        if line.endswith("map:"):
            for id_, new in id_to_new.items():
                if new is None:
                    id_to_new[id_] = id_
            id_to_new = dict.fromkeys(id_to_new.values())
            continue
        new, start, range_ = map(int, line.split())
        end = start + range_ - 1
        for id_ in id_to_new.keys():
            if start <= id_ <= end:
                id_to_new[id_] = new + (id_ - start)

    for id_, new in id_to_new.items():
        if new is None:
            id_to_new[id_] = id_
    print(min(id_to_new.values()))



solve()