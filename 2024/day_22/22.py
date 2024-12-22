from collections import Counter, deque

from utils import read_input

SEQUENCES = Counter()


def solve():
    lines = read_input().split('\n')
    ans = 0
    for line in lines:
        ans += calc_secret(int(line))
    print("p1:", ans)
    print("p2:", max(SEQUENCES.items(), key=lambda x: x[1]))


def calc_secret(sec_num):
    prev = int(str(sec_num)[-1])
    sequences = deque([])
    seq_to_score = {}
    for _ in range(2000):
        cur = int(str(sec_num)[-1])
        sequences.append(cur - prev)
        if len(sequences) > 4:
            sequences.popleft()
        if len(sequences) == 4:
            sq_t = tuple(sequences)
            if sq_t not in seq_to_score:
                seq_to_score[sq_t] = cur
        prev = cur
        res = sec_num * 64
        sec_num = mix(sec_num, res)
        sec_num = prune(sec_num)

        res = sec_num // 32
        sec_num = mix(sec_num, res)
        sec_num = prune(sec_num)

        res = sec_num * 2048
        sec_num = mix(sec_num, res)
        sec_num = prune(sec_num)
    for seq, score in seq_to_score.items():
        SEQUENCES[seq] += score
    return sec_num


def mix(sec_num, num):
    return sec_num ^ num


def prune(sec_num):
    return sec_num % 16777216


if __name__ == "__main__":
    # calc_secret(123)
    solve()
