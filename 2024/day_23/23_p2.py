from collections import defaultdict
from utils import read_input


def solve():
    lines = read_input().split("\n")
    graph = defaultdict(set)
    for line in lines:
        from_, to = line.split("-")
        graph[from_].add(to)
        graph[to].add(from_)

    max_seen = set()
    for ver, neighbors in graph.items():
        seen = {ver}
        for neigh in neighbors:
            if seen <= graph[neigh]:
                seen.add(neigh)
        if len(seen) > len(max_seen):
            max_seen = seen
    print(",".join(sorted(max_seen)))


if __name__ == "__main__":
    solve()
