from collections import defaultdict


def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip().split("|") for line in f]
    return lines


def solve():
    input_ = read_input()
    sum_ = 0

    max_card_id = len(input_)
    card_count = defaultdict(int)

    p2_sum = 0
    for c in range(1, max_card_id + 1):
        card_count[c] = 1
    for card in input_:
        cw = card[0].split()
        _, card_id, winning_nums = cw[0], cw[1][:-1], cw[2:]
        winning_nums = set(winning_nums)
        my_nums = card[1].split()
        my_nums = set(my_nums)

        matched = winning_nums.intersection(my_nums)
        # part1
        # print(matched)
        # points = 1 if matched else 0
        # for _ in range(1, len(matched)):
        #     points *= 2
        # sum_ += points
        card_copies = len(matched)
        multiplier = card_count[int(card_id)]
        for c_id in range(int(card_id) + 1, int(card_id) + card_copies + 1):
            if c_id > max_card_id:
                break
            card_count[int(c_id)] += 1 * multiplier
    print(sum(card_count.values()))


solve()
