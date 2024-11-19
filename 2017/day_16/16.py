from itertools import cycle


def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip().split(',') for line in f]
    return lines


def solve():
    inp = read_input()[0]
    programs = list('abcdefghijklmnop')
    total_moves = 1000000000 * len(inp)
    seen = {}
    cnt = 0
    cycle_found = False
    for action in cycle(inp):
        if cnt == total_moves:
            return ''.join(programs)
        if action[0] == 's':
            programs = programs[-int(action[1:]):] + programs[:-int(action[1:])]
        elif action[0] == 'x':
            d1, d2 = action[1:].split('/')
            d1, d2 = int(d1), int(d2)
            p1_tmp = programs[d1]
            programs[d1] = programs[d2]
            programs[d2] = p1_tmp
        elif action[0] == 'p':
            p1, p2 = action[1:].split('/')
            d1, d2 = programs.index(p1), programs.index(p2)
            p1_tmp = programs[d1]
            programs[d1] = programs[d2]
            programs[d2] = p1_tmp
        cnt += 1
        pr_s = ''.join(programs)
        if pr_s in seen and not cycle_found:
            print(f'cycle in {cnt}')
            cycle_size = cnt - seen[pr_s]
            print(f'cycle size {cycle_size}')
            # -1 because 1 cycle done already
            remaining = total_moves // cycle_size - 1
            # skipping the remaining number of cycles, then continue as usual the rest of the steps
            cnt += cycle_size * remaining
            cycle_found = True
        # the 1st position repeats after certain cnt number of permutations so don't need to remember all positions
        if cnt == 1:
            seen[pr_s] = cnt



if __name__ == "__main__":
    print(solve())
