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
        if i+1 < len(line):
            disk_map.extend(["."] * int(line[i + 1]))

    new_disk = disk_map[:]
    # print(new_disk)
    for i, num in enumerate(disk_map[::-1]):
        if num == ".":
            continue
        else:
            new_disk[-i-1] = "."

            free = new_disk.index(".")
            new_disk[free] = num
    print(new_disk)
    for i, n in enumerate(new_disk):
        if n == ".":
            break
        ans += i*int(n)
    submit(ans, 1)


def solve_p2():
    line = read_input()[0]
    ans = 0
    print(line)
    file_map = []
    free_map = []
    for i in range(0, len(line), 2):
        id_ = i // 2
        # id, size, idx
        file_map.append((id_, int(line[i])))
        if i+1 < len(line):
            free_map.append(int(line[i+1]))

    new_disk = defaultdict(list)
    moved = set()
    for j, (fid, fsize) in enumerate(file_map[::-1]):
        real_j = len(file_map)-j-1
        for i, free in enumerate(free_map):
            if i >= real_j:
                break
            if free >= fsize:
                free_map[i] -= fsize
                new_disk[i].append((fid, fsize))
                moved.add((fid, fsize))
                break
    file_map = [f for f in file_map]
    nd_repr = []
    i = 0
    while i < len(file_map):
        # file
        id_, size = file_map[i]
        if (id_, size) in moved:
            nd_repr.extend(["."]*size)
        else:
            nd_repr.extend([id_]*size)
        #free
        if new_disk[i]:
            for f in new_disk[i]:
                nd_repr.extend([f[0]]*f[1])
        if i < len(free_map):
            nd_repr.extend(["."]*free_map[i])
        i += 1

    # new disk free_i: file_id, file_size
    for i, n in enumerate(nd_repr):
        if n == ".":
            continue
        ans += i*int(n)
    # 8587288893605 too high
    submit(ans, 2)


if __name__ == "__main__":
    # solve_p1()
    solve_p2()
