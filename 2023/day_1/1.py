import re

from utils import read_input, digits


def solve():
    input_ = read_input()
    print(input_)
    res = 0
    for line in input_:
        print(line)
        line = replace_n(line)
        d = digits(line)
        print(d)
        res += int(d[0] + d[-1])
    print(res)


def replace_n(line):
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
    reg = re.findall("(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
    first, last = reg[0], reg[-1]
    first = str(digits[first]) if first in digits else first
    last = str(digits[last]) if last in digits else last
    return first + last


if __name__ == "__main__":
    solve()
