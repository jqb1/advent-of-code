def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


def solve():
    input_ = read_input()
    print(input_)
    s = 0
    for line in input_:
        n_now = ""
        curr_line = ""
        for ch in line:
            curr_line += ch
            if ch.isnumeric():
                n_now += ch
                break
            nw_str = replace_numbers(curr_line)
            if nw_str != curr_line:
                n_now += nw_str[-1]
                break
        curr_line = ""
        for ch in line[::-1]:
            curr_line = ch + curr_line
            if ch.isnumeric():
                n_now += ch
                break
            nw_str = replace_numbers(curr_line)
            if nw_str != curr_line:
                n_now += nw_str[0]
                break
        print(line, n_now[0] + n_now[-1])
        s += int(n_now[0] + n_now[-1])
    return s


def replace_numbers(s):
    digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    for name, digit in digits.items():
        s = s.replace(name, str(digit))
    return s


solution = solve()
