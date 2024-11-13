def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


def main():
    lengths = (2, 4, 3, 7)
    len_to_digit = {
        2: 1,
        3: 7,
        4: 4,
        7: 8,
    }
    c = 0
    s = 0
    for line in read_input():
        sig_pattern = line.split("|")[0].rstrip().split()
        result = line.split("|")[1].strip().split()
        digit_to_signal = {}
        for sig in sig_pattern:
            if len(sig) in lengths:
                c += 1
                digit_to_signal[len_to_digit[len(sig)]] = sig
        for sig in sig_pattern:
            if len(sig) == 6:
                if len(set(digit_to_signal[1]) & set(sig)) == 1:
                    digit_to_signal[6] = sig
                elif len(set(digit_to_signal[4]) & set(sig)) == 3:
                    digit_to_signal[0] = sig
                else:
                    digit_to_signal[9] = sig
        for sig in sig_pattern:
            if len(sig) == 5:
                if len(set(digit_to_signal[1]) & set(sig)) == 2:
                    digit_to_signal[3] = sig

                elif len(set(digit_to_signal[6]) & set(sig)) == 5:
                    digit_to_signal[5] = sig
                else:
                    digit_to_signal[2] = sig
        decoded = ""
        for signal in result:
            if d := len_to_digit.get(len(signal)):
                decoded += str(d)
            else:
                for dig, sig in digit_to_signal.items():
                    if set(signal) == set(sig):
                        decoded += str(dig)
                        break
        s += int(decoded)

    print(c)
    print(s)


if __name__ == "__main__":
    main()
