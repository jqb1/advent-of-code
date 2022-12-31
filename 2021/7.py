def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


def main():
    crabs = list(map(int, read_input()[0].split(',')))
    cheapest = 10e7

    for pos in range(min(crabs), max(crabs)+1):
        pos_change_cost = sum((1 + abs(pos-n))/2 * abs(pos-n) for n in crabs)
        cheapest = min(cheapest, pos_change_cost)

    print(cheapest)


if __name__ == "__main__":
    main()