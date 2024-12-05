from collections import defaultdict

from utils import read_input


def solve():
    lines = read_input()
    c_to_copies = defaultdict(int)
    for line in lines:
        p1, p2 = line.split("|")
        _, cid, *w_nums = p1.split()
        cid = int(cid[:-1])
        c_to_copies[cid] += 1
        m_nums = p2.split()
        matches = len(set(m_nums) & set(w_nums))
        cur_copies = c_to_copies[cid]
        if cid <= len(lines):
            for i in range(cid, cid + matches + 1):
                c_to_copies[i] += cur_copies
    print(sum(c_to_copies.values()) / 2)


if __name__ == "__main__":
    solve()
