from collections import defaultdict, deque

from utils import read_input, submit, ints


def solve_p1():
    lines = read_input().split("\n")
    ans = 0

    before = defaultdict(list)
    after = defaultdict(list)
    produce = []
    for line in lines:
        if "|" in line:
            ba = map(int, ints(line))
            bef, aft = ba
            before[aft].append(bef)
            after[bef].append(aft)
        elif line:
            produce.append(list(map(int, ints(line))))
    correct = []
    for order in produce:
        seen = set()
        valid = True
        for num in order:
            bef, aft = before[num], after[num]
            if not check_valid(bef, aft, seen, set(order)):
                valid = False
            seen.add(num)
        if valid:
            correct.append(order)
    for c in correct:
        mid = len(c) // 2
        ans += c[mid]
    # submit(ans, 1)
    print(ans)


def solve_p2():
    lines = read_input().split("\n")
    ans = 0

    before = defaultdict(list)
    after = defaultdict(list)
    produce = []
    for line in lines:
        if "|" in line:
            ba = map(int, ints(line))
            bef, aft = ba
            before[aft].append(bef)
            after[bef].append(aft)
        elif line:
            produce.append(list(map(int, ints(line))))

    correct = []
    incorrect = []
    for order in produce:
        seen = set()
        valid = True
        for num in order:
            bef, aft = before[num], after[num]
            if not check_valid(bef, aft, seen, set(order)):
                valid = False
            seen.add(num)
        if valid:
            correct.append(order)
        else:
            incorrect.append(order)

    correct = []
    print(incorrect)
    for o in incorrect:
        correct.append(top_sort(o, before, after))

    for c in correct:
        mid = len(c) // 2
        ans += c[mid]
    print(correct)
    print(ans)


def check_valid(before, after, seen, order):
    for num in before:
        if num not in seen and num in order:
            return False
    for num in after:
        if num in seen and num in order:
            return False
    return True


def top_sort(pat, before, after):
    pat = set(pat)
    n_to_r = {}
    # filter edges to nonexistent numbers
    for n in pat:
        b, a = before[n], after[n]
        b = {el for el in b if el in pat}
        a = {el for el in a if el in pat}
        n_to_r[n] = b, a
    graph = defaultdict(list)
    deg = defaultdict(int)
    for n, r in n_to_r.items():
        bef, af = r
        for b in bef:
            graph[n].append(b)
            deg[b] += 1
        for a in af:
            graph[a].append(n)
            deg[n] += 1
    q = deque([n for n in pat if deg[n] == 0])
    new_order = []
    # topsort
    while q:
        # remove a node n from S
        node = q.popleft()
        # add n to L
        new_order.append(node)
        for to in graph[node]:
            deg[to] -= 1
            if deg[to] == 0:
                q.append(to)
    return new_order


if __name__ == "__main__":
    # solve_p1()
    solve_p2()
