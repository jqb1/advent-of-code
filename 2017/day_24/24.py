from collections import deque, defaultdict

from utils import read_input, submit


def solve():
    lines = read_input(0).split("\n")
    q = deque([])
    ports = defaultdict(list)
    for line in lines:
        p1, p2 = map(int, line.split("/"))
        if p1 == 0:
            q.append((p2, 0, f"{p1},{p2}", set()))
        else:
            ports[p1].append(p2)
            if p1 != p2:
                ports[p2].append(p1)
    strongest = 0
    seen = set()
    while q:
        p, st, path, used = q.popleft()
        if path in seen:
            continue
        seen.add(path)
        st += p
        strongest = max(strongest, st)
        for posp in ports[p]:
            if (p, posp) in used or (posp, p) in used:
                continue
            q.append((posp, st + p, path + f", {p},{posp}", used | {(p, posp)}))

    submit(strongest, 1)


def solve_p2():
    lines = read_input()
    q = deque([])
    ports = defaultdict(list)
    for line in lines:
        p1, p2 = map(int, line.split("/"))
        if p1 == 0:
            q.append((p2, 0, f"{p1},{p2}", set()))
        else:
            ports[p1].append(p2)
            if p1 != p2:
                ports[p2].append(p1)
    longest = []
    longest_len = 0
    seen = set()
    while q:
        p, st, path, used = q.popleft()
        if path in seen:
            continue
        seen.add(path)
        st += p
        if len(path) >= longest_len:
            if len(path) == longest_len:
                longest.append(st)
            else:
                longest = [st]
            longest_len = len(path)

        for posp in ports[p]:
            if (p, posp) in used or (posp, p) in used:
                continue
            q.append((posp, st + p, path + f", {p},{posp}", used | {(p, posp)}))

    submit(max(longest), 2)


if __name__ == "__main__":
    # solve()
    solve_p2()
