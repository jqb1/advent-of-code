from collections import defaultdict
from itertools import permutations

from utils import read_input, digits

NUM_KBR = {
    button: (r, c)
    for r, row in enumerate(("789", "456", "123", " 0A"))
    for c, button in enumerate(row)
}
DIR_KBR = {
    button: (r, c)
    for r, row in enumerate((" ^A", "<v>"))
    for c, button in enumerate(row)
}


def solve():
    lines = read_input().split("\n")

    s_pos = "A"  # starts at A
    ans = 0
    for line in lines:
        res = move_num_kbr(s_pos, line, "num")
        print(res, len(res))
        cur_res = res

        for i in range(2):
            new_res = []
            for p in cur_res:
                patterns = move_num_kbr(s_pos, p, "dir")
                new_res.extend(patterns)
                # print(pat, len(pat), pattern_cost(pat))
            cur_res = new_res

        shortest = get_shortest(cur_res)
        print(line, len(shortest))
        ans += len(shortest) * int("".join(digits(line)))
    # 136780 good
    print("ans", ans)


def get_shortest(patterns):
    return sorted(patterns, key=lambda x: len(x))[0]


def pattern_cost(pat):
    prev = "A"
    steps = 0
    for p in pat:
        p1, p2 = DIR_KBR[prev], DIR_KBR[p]
        d = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        steps += d
        prev = p
    return steps


def move_num_kbr(cur_pos: str, inp: str, kbr_type: str):
    if not inp:
        return ""
    next_pos = inp[0]
    patterns = set()
    kbr = NUM_KBR if kbr_type == "num" else DIR_KBR

    for pat in paths_between(cur_pos, next_pos, kbr):
        pat += "A"
        if validate_pat(pat, cur_pos, kbr):
            patterns.add(pat)
    down_paths = move_num_kbr(next_pos, inp[1:], kbr_type)
    if not down_paths:
        return patterns
    return [pat + down_pat for down_pat in down_paths for pat in patterns]


def validate_pat(pat: str, cur_p: str, lookup: dict):
    # check if pattern invalid based on shortest path between cur_p and empty space
    path_to_gap, _ = paths_between(cur_p, " ", lookup)
    if pat.startswith(path_to_gap):
        return False
    return True


def paths_between(p1: str, p2: str, lookup: dict):
    k_cur, k_next = lookup[p1], lookup[p2]
    dr, dc = (k_next[0] - k_cur[0], k_next[1] - k_cur[1])
    rmove = "^" if dr < 0 else "v"
    cmove = ">" if dc > 0 else "<"
    # best path will always be all rows first then columns
    # or all cols then rows (one of those because we can't step on a gap)
    return rmove * abs(dr) + cmove * abs(dc), cmove * abs(dc) + rmove * abs(dr)


if __name__ == "__main__":
    assert validate_pat("vvv", "7", NUM_KBR) is False
    assert validate_pat("vv", "4", NUM_KBR) is False
    assert validate_pat("v", "1", NUM_KBR) is False
    assert validate_pat("v>vv", "7", NUM_KBR) is True
    assert validate_pat("<<^", "A", NUM_KBR) is False

    assert validate_pat("^>>", "<", DIR_KBR) is False
    assert validate_pat("^>", "<", DIR_KBR) is False
    assert validate_pat("<v", "^", DIR_KBR) is False
    assert validate_pat("^>", "v", DIR_KBR) is True
    assert pattern_cost("^<>^") == 1 + 2 + 2 + 2 == pattern_cost("^<>>^^^")
    assert pattern_cost("<A") == 3 + 3
    solve()
