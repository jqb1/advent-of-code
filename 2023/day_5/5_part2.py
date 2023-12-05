def read_input():
    with open("./input.txt") as f:
        lines = f.read()
    return lines


def solve():
    input_ = read_input()
    seeds, *maps = input_.split("\n\n")
    ranges = get_ranges(seeds)
    # for each seed range, go through the entire path
    # on each map, map current rage, split range if not fitting in one
    result_ranges = process_seeds(ranges, maps)
    result_min = min(result_ranges, key=lambda x: x[0])
    print(result_min[0])


def process_seeds(seed_ranges, maps):
    output_ranges = seed_ranges
    for map_ in maps:
        map_ = map_.split("\n")
        output_ranges = process_map(output_ranges, map_[1:])
    return output_ranges


def process_map(input_ranges, map_):
    output_ranges = []
    ranges_to_map = [*input_ranges]
    while ranges_to_map:
        curr_range = ranges_to_map.pop()
        mapped = False
        for line in map_:
            new, r_start, r_len = [int(n) for n in line.split()]
            r_end = r_start + r_len
            mapped_ranges, split_ranges = process_range(curr_range, new, r_start, r_end)
            if split_ranges:
                ranges_to_map.extend(split_ranges)
            if mapped_ranges:
                mapped = True
                output_ranges.extend(mapped_ranges)
                break
        # if not mapped, don't change
        if not mapped:
            output_ranges.append(curr_range)
    return output_ranges


def process_range(curr_range, new, r_start, r_end):
    # 3 split possibilities
    # 1. whole range in new range, right/left part of range in new range,
    # 2. right/left part of range in new range
    # 3. middle part of range in new range

    # whole mapped
    # r_start ... cur_range[0] ... cur_range[1] ... r_end
    if r_end > curr_range[0] >= r_start and r_start <= curr_range[1] < r_end:
        diff = curr_range[0] - r_start
        diff2 = curr_range[1] - r_start
        return [(diff + new, diff2 + new)], []
    # left part in range
    # r_start ... [cur_range[0] ... r_end] ... cur_range[1]
    elif r_start < curr_range[0] < r_end <= curr_range[1]:
        diff = curr_range[0] - r_start
        diff2 = r_end - r_start
        return [(diff + new, diff2 + new)], [(r_end, curr_range[1])]
    # right part in range
    # cur_range[0] ... [r_start .... cur_range[1]] ... r_end
    elif r_start < curr_range[1] < r_end:
        diff2 = curr_range[1] - r_start
        return [(new, new + diff2)], [(curr_range[0], r_start)]
    # middle part in range
    # cur_range[0] ... [r_start .... r_end] ... cur_range[1]
    elif curr_range[0] < r_start and curr_range[1] >= r_end:
        return [(new, r_end - r_start + new)], [(curr_range[0], r_start), (r_end, curr_range[1])]
    else:
        return [], []


def get_ranges(seeds):
    start = None
    ranges = []
    for s in seeds.split()[1:]:
        if start:
            ranges.append((int(start), int(start) + int(s)))
            start = None
        else:
            start = s
    return ranges


solve()


def test_process_range():
    # whole in range
    res = process_range((10, 15), 5, 8, 18)
    assert res == ([(7, 12)], [])
    # left part in range
    res = process_range((10, 18), 5, 8, 15)
    assert res == ([(7, 12)], [(15, 18)])
    # right part in range
    res = process_range((3, 12), 5, 8, 15)
    assert res == ([(5, 9)], [(3, 8)])
    # middle in range
    res = process_range((3, 15), 5, 10, 12)
    # (10, 12) mapped ->
    assert res == ([(5, 7)], [(3, 10), (12, 15)])


# test_process_range()
