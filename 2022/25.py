def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


def main():
    snafu_numbers = read_input()
    num_sum = 0
    for num in snafu_numbers:
        num_dec = 0
        for i, digit in enumerate(num[::-1]):
            if digit in ('-', '='):
                num_dec += 5**i * (-2 if digit == '=' else -1)
            else:
                num_dec += 5**i*int(digit)
        num_sum += num_dec
    print(num_sum)

    s = ''
    d = num_sum
    tr = 0
    while d != 0:
        d += tr
        d, m = divmod(d, 5)
        if tr:
            s = s[:-1]
        if m in (3, 4):
            s += '=1' if m == 3 else '-1'
            tr = 1
        else:
            s += str(m)
            tr = 0
    s = s[::-1]
    print(s)


if __name__ == "__main__":
    main()