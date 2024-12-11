from utils import read_input, submit


def solve():
    lines = read_input().split('\n')
    print(lines)
    ans = 0
    for line in lines:
        line = list(map(int, line.split()))
        if check_correct(line):
            ans += 1
        else:
            if validate_more(line):
                ans += 1

    submit(ans, 1)


def validate_more(line):
    for i in range(len(line)):
        if check_correct(line[:i] + line[i + 1 :]):
            return True
    return False


def check_correct(line):
    t = set()
    for i, el in enumerate(line):
        diff = line[i - 1] - el
        if i == 0:
            continue
        t.add(diff < 0)
        if (abs(diff) > 3 or abs(diff) < 1) or len(t) > 1:
            return False
    if len(set(t)) == 1:
        return True
    return False


if __name__ == "__main__":
    solve()
