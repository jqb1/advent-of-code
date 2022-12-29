def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


OPERATION = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x / y,
    "*": lambda x, y: x * y,
}


def main():
    monkeys = {line.split(":")[0]: line.split(":")[1].lstrip() for line in read_input()}
    res = calculate_operation(monkeys, monkeys["root"])
    print(res)


def calculate_operation(monkeys, operation):
    if operation.isnumeric():
        return int(operation)
    else:
        v1, operator, v2 = operation.split()
        if v1 == "humn":
            v2 = calculate_operation(monkeys, monkeys[v2])
            return f"(x{operator}{v2})"

        v1 = calculate_operation(monkeys, monkeys[v1])
        v2 = calculate_operation(monkeys, monkeys[v2])

        if isinstance(v1, str) or isinstance(v2, str):
            if operation == "qhbp + vglr":
                return f"{v1} = {v2}"
            return f"({v1}{operator}{v2})"

        return int(OPERATION[operator](v1, v2))


if __name__ == "__main__":
    main()
