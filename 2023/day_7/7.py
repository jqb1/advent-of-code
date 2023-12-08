from collections import defaultdict

def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


# card_to_strength = {c: s for s, c in enumerate(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"][::-1], 1)}
# part 2
card_to_strength = {c: s for s, c in enumerate(["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"][::-1], 1)}


def solve():
    input_ = read_input()

    score_to_hand = defaultdict(list)
    hand_to_bid = {}
    for line in input_:
        hand, bid = line.split()
        bid = int(bid)
        hand_to_bid[hand] = bid
        cards = count_cards(hand)

        for f in [get_kind_score, get_house_score, get_pair, get_high_card]:
            result = f(cards)
            if result:
                if "J" in cards:
                    print("before ", result, hand)
                    result = process_cards_with_joker(hand, result, cards)
                    print("after ", result)
                score_to_hand[result].append(hand)
                break

    score_to_hand = sort_same_rank_cards(score_to_hand)
    print(score_to_hand.values())
    rank = 0
    result = 0
    for score in sorted(score_to_hand):
        for hand in score_to_hand[score]:
            rank += 1
            result += (rank * hand_to_bid[hand])
    print(result)


def sort_same_rank_cards(score_to_hand):
    new_score_to_hand = {}
    for score, hands in score_to_hand.items():
        new_hands = sort_hands(hands)
        new_score_to_hand[score] = new_hands
    return new_score_to_hand


def sort_hands(hands):
    hand_to_score = {}
    for hand in hands:
        hand_score = []
        for card in hand:
            hand_score.append(card_to_strength[card])
        hand_to_score[hand] = hand_score

    return sorted(hands, key=lambda h: hand_to_score[h])


def process_cards_with_joker(hand, org_score, cards):
    biggest = org_score
    sorted_cards = sorted(cards.items(), key=lambda x: x[1])
    most_common = sorted_cards[-1]
    if most_common[0] == "J":
        if most_common[1] == 5:
            return 7
        most_common = sorted_cards[-2]
    cards[most_common[0]] += cards["J"]
    del cards["J"]
    for f in [get_kind_score, get_house_score, get_pair, get_high_card]:
        result = f(cards)
        if result and result > biggest:
            biggest = result
            break
    return biggest


def count_cards(hand):
    cards = defaultdict(int)
    for card in hand:
        cards[card] += 1
    return cards


# 5 kind - 7, 4 kind - 6, 3 kind - 4
def get_kind_score(cards):
    # 5 kind
    if len(cards) == 1:
        return 7
    if any(count == 4 for count in cards.values()):
        return 6
    if sorted(cards.values()) == [1, 1, 3]:
        return 4


# house - 5
def get_house_score(cards):
    if set(cards.values()) == {3, 2}:
        return 5


# two pair
def get_pair(cards):
    # 2 2 1
    if sorted(cards.values()) == [1, 2, 2]:
        return 3

    if sorted(cards.values()) == [1, 1, 1, 2]:
        return 2


def get_high_card(cards):
    if len(cards) == 5:
        return 1


solve()
