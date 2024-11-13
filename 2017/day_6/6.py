def read_input():
    with open("./input.txt") as f:
        lines = [[int(x) for x in line.rstrip().split()] for line in f]
    return lines


def solve():
    blocks = read_input()[0]
    seen = set()
    cycles = 0
    block_to_step = {}
    while True:
        max_i = 0
        max_el = blocks[0]
        if tuple(blocks) in seen and cycles > 0:
            return cycles - block_to_step[tuple(blocks)]
        seen.add(tuple(blocks))
        block_to_step[tuple(blocks)] = cycles
        for i, el in enumerate(blocks):
            if el > max_el:
                max_el = el
                max_i = i
        add_c, rest = divmod(max_el, len(blocks) - 1)
        to_add = max_el
        i = max_i + 1
        blocks[max_i] = 0
        while to_add:
            if i == len(blocks):
                i = 0
            if add_c and to_add >= add_c:
                blocks[i] += add_c
                to_add -= add_c
            else:
                blocks[i] += 1
                to_add -= 1
            i += 1
        print(blocks)
        cycles += 1


print(solve())
