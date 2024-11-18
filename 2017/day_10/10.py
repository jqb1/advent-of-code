from functools import reduce


def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


def knot_hash(input_):
    lengths = list(map(ord, input_)) + [17, 31, 73, 47, 23]
    lsize = 256
    hash_out = [i for i in range(lsize)]
    # - Reverse the order of that length of elements in the list, starting with the element at the current position.
    # - Move the current position forward by that length plus the skip size.
    # - Increase the skip size by one.
    cur_pos = 0
    skip_size = 0
    for i in range(64):
        for l in lengths:
            sub_list = (
                hash_out[cur_pos : cur_pos + l]
                if cur_pos + l < lsize
                else hash_out[cur_pos:] + hash_out[: (cur_pos + l) % lsize]
            )
            sub_list = sub_list[::-1]
            for s_i in range(len(sub_list)):
                hash_out[(cur_pos + s_i) % lsize] = sub_list[s_i]
            cur_pos += l + skip_size
            cur_pos = cur_pos % lsize
            skip_size += 1
    res = []
    for xi in range(0, 256, 16):
        cur_res = reduce(lambda x, y: x ^ y, hash_out[xi : xi + 16])
        res.append(cur_res)
    res = "".join([f"{r:02x}" for r in res])
    print(res)
    return res


if __name__ == "__main__":
    knot_hash(read_input()[0])
