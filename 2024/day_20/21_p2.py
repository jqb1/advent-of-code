from functools import cache

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
    s_pos = "A"
    ans = 0
    for line in lines:
        num_kbr_moves = move_num_kbr(s_pos, line, "num")
        paths = [find_min_dir_press(pat, 25) for pat in num_kbr_moves]
        ans += min(paths) * int("".join(digits(line)))
        print(ans)
    print(ans)


@cache
def find_min_dir_press(pat: str, depth: int):
    # last robot
    if depth == 0:
        return len(pat)

    all_lengths = 0
    pat = "A" + pat
    for pi, press in enumerate(pat[:-1]):
        all_lengths += min(
            find_min_dir_press(p + "A", depth - 1)
            for p in paths_between(press, pat[pi + 1], DIR_KBR)
            if validate_pat(p, press, DIR_KBR)
        )
    return all_lengths


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
    solve()
