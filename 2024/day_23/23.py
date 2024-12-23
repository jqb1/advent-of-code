from collections import defaultdict

from utils import read_input


def solve():
    lines = read_input().split('\n')
    graph = defaultdict(list)
    for line in lines:
        from_, to = line.split('-')
        graph[from_].append(to)
        graph[to].append(from_)

    sets_of_3 = set()
    for from_, to in graph.items():
        paths = go_depth(graph, 3, from_, [])
        sets_of_3.update(paths)
    ans = 0
    for s in sets_of_3:
        if any(n for n in s if n[0] == 't'):
            ans += 1
    print(sets_of_3)
    print(ans)


def go_depth(graph, steps, cur_n, path: list) -> set:
    if steps == 0:
        if cur_n == path[0]:
            return {tuple(sorted(path))}
        return set()
    all_paths = set()
    if not set(path) <= set(graph[cur_n]):
        return set()
    for neighbor in graph[cur_n]:
        paths = go_depth(graph, steps - 1, neighbor, path + [cur_n])
        all_paths |= paths
    return all_paths


if __name__ == "__main__":
    solve()
