from collections import deque


def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip().split() for line in f]
    return lines


def solve():
    inp = read_input()
    a_val, b_val = int(inp[0][-1]), int(inp[1][-1])
    a_factor, b_factor = 16807, 48271
    div_val = 2147483647
    match_c = 0
    # p2
    a_q, b_q = deque([]), deque([])
    comparisons = 0
    while comparisons <= (5 * 10 ** 6):
        a_val = (a_val * a_factor) % div_val
        b_val = (b_val * b_factor) % div_val
        if a_val % 4 == 0:
            a_bin = bin(a_val)
            a_q.append(a_bin)
        if b_val % 8 == 0:
            b_bin = bin(b_val)
            b_q.append(b_bin)
        if a_q and b_q:
            a, b = a_q.popleft(), b_q.popleft()
            if a[-16:] == b[-16:]:
                match_c += 1
            comparisons += 1
    print(match_c)


if __name__ == "__main__":
    solve()
