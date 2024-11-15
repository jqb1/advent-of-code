from collections import deque


def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip().split(' <-> ') for line in f]
    return lines


def solve():
    inp = read_input()
    connected = set()
    neighbors = {line[0]: line[1].split(', ') for line in inp}
    group_cnt = 0
    for n in neighbors:
        if n in connected:
            continue
        q = deque([n])
        group_cnt += 1
        while q:
            cur = q.popleft()
            if cur in connected:
                continue
            connected.add(cur)
            for neighbor in neighbors[cur]:
                if neighbor in connected:
                    continue
                q.append(neighbor)
    print(group_cnt)
    print(len(connected))


solve()
