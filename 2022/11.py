from collections import defaultdict


def read_input():
    with open("./input.txt") as f:
        moves = [line_.rstrip() for line_ in f]
    return moves


def find_divisor(num, all_divisors_):
    # modulos = [(num % div_) for div_ in all_divisors_]
    mul = 1
    for div in all_divisors_:
        mul *= div
    return num % mul

    # for i in range(2, num // 2):
    #     modulos2 = [int(i % div_) for div_ in all_divisors_]
    #     if modulos == modulos2:
    #         return i
    # return num


lines = read_input()

monkeys = defaultdict(list)
monkeys_inspections = defaultdict(int)

all_divisors = []
for round_ in range(10000):
    print(round_)
    for line_idx in range(0, len(lines), 7):
        items = []
        monkey = None
        operation, divisible_by, if_true_monkey, if_false_monkey = (
            None,
            None,
            None,
            None,
        )
        for l_ in range(6):
            line = lines[line_idx + l_]
            if not line:
                continue
            # print(lines[line_idx+l_])
            if l_ == 0:
                monkey = int(line.split()[1][0])
            elif l_ == 1:
                if round_ == 0:
                    items = list(
                        map(
                            int,
                            line.replace("Starting items:", "")
                            .replace(" ", "")
                            .split(","),
                        )
                    )
                    for it in items:
                        monkeys[monkey].append(it)
                else:
                    items = monkeys[monkey]
            elif l_ == 2:
                operation = line.replace("Operation: new = ", "").lstrip()
            elif l_ == 3:
                divisible_by = int(line.replace("Test: divisible by ", "").lstrip())
                if round_ == 0:
                    all_divisors.append(divisible_by)
            elif l_ == 4:
                if_true_monkey = int(
                    line.replace("If true: throw to monkey ", "").lstrip()
                )
            elif l_ == 5:
                if_false_monkey = int(
                    line.replace("If false: throw to monkey ", "").lstrip()
                )

        for item in monkeys[monkey]:
            monkeys_inspections[monkey] += 1
            old = item
            new = eval(operation)

            if round_ > 0:
                new = find_divisor(new, all_divisors)
            if new % divisible_by == 0:
                monkeys[if_true_monkey].append(new)
            else:
                monkeys[if_false_monkey].append(new)
        monkeys[monkey].clear()
    if round_ == 0:
        print(monkeys.values())
print(monkeys.items())
print(monkeys_inspections.values())
