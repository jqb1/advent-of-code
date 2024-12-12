from collections import deque, defaultdict

from utils import read_input, submit


def solve_p1():
    line = read_input(1)[0]
    ans = 0
    print(line)
    disk_map = []
    for i in range(0, len(line), 2):
        id_ = i // 2
        disk_map.extend([id_] * int(line[i]))
        if i + 1 < len(line):
            disk_map.extend(["."] * int(line[i + 1]))

    new_disk = disk_map[:]
    for i, num in enumerate(disk_map[::-1]):
        if num == ".":
            continue
        else:
            new_disk[-i - 1] = "."
            free = new_disk.index(".")
            new_disk[free] = num

    for i, n in enumerate(new_disk):
        if n == ".":
            break
        ans += i * int(n)
    print("part1", ans)


def solve_p2():
    line = read_input().split("\n")[0]
    ans = 0
    file_map = []
    free_map = []
    new_map = []
    cur_pos = 0
    for i in range(0, len(line), 2):
        id_ = i // 2
        fsize = int(line[i])
        file_map.append((cur_pos, fsize))
        new_map.extend([id_] * fsize)
        cur_pos += fsize
        if i + 1 < len(line):
            free_size = int(line[i + 1])
            free_map.append((cur_pos, free_size))
            new_map.extend(["."] * free_size)
            cur_pos += free_size

    for fi, fsize in file_map[::-1]:
        for i, (free_start, free_size) in enumerate(free_map):
            if free_start >= fi:
                break
            assert free_start < fi
            if free_size >= fsize:
                new_map[free_start : free_start + fsize] = new_map[fi : fi + fsize]
                new_map[fi : fi + fsize] = ["."] * fsize
                free_map[i] = (free_start + fsize, free_size - fsize)
                break

    for i, n in enumerate(new_map):
        if n == ".":
            continue
        ans += i * int(n)
    print("par2:", ans)


if __name__ == "__main__":
    # solve_p1()
    solve_p2()
