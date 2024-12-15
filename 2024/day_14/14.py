from collections import Counter
from functools import reduce

from utils import read_input, ints


def solve():
    lines = read_input().split("\n")
    robots = []
    rsize, csize = 103, 101
    # rsize, csize = 7, 11
    for i, line in enumerate(lines):
        pc, pr, vc, vr = ints(line)
        robots.append(((pr, pc), (vr, vc)))

    for tick in range(10000):
        new_robots = []
        map_pos = Counter()
        for (rr, rc), (vr, vc) in robots:
            rr += vr
            rc += vc
            rr %= rsize
            rc %= csize
            new_robots.append(((rr, rc), (vr, vc)))
            map_pos[rr, rc] += 1
        if tick % 100 == 0:
            print_map(rsize, csize, map_pos, tick)
        if all(v == 1 for p, v in map_pos.items()):
            print_map(rsize, csize, map_pos, tick)
            print("sec:", tick)
            break
        robots = new_robots

    positions = Counter()
    sq_r_size = rsize // 2
    sq_c_size = csize // 2
    mid_r = sq_r_size
    mid_c = sq_c_size
    for pos, _ in robots:
        r, c = pos
        if r == mid_r or c == mid_c:
            continue
        if r > mid_r:
            r -= 1
        if c > mid_c:
            c -= 1
        sq_r = r // sq_r_size
        sq_c = c // sq_c_size
        positions[sq_r, sq_c] += 1
    print("p1:", reduce(lambda x, y: x * y, positions.values()))


def print_map(rsize, csize, map_pos, sec):
    fs = ""
    for r in range(rsize):
        row = " ".join(["X" if (r, c) in map_pos else "." for c in range(csize)])
        fs += f"{row}\n"
    print(fs)
    print(f"SEC:{sec+1}\n\r")


if __name__ == "__main__":
    solve()
