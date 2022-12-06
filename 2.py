with open("/Users/jkoziol/Downloads/input.txt") as f:
    records = f.readlines()
    records = [l.rstrip() for l in records]

scores = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def result(oppo, play):
    oppo = {"A": "rock", "B": "paper", "C": "scissors"}[oppo]
    # my = {"X": "rock", "Y": "paper", "Z": "scissors"}[my]
    scores = {"rock": 1, "paper": 2, "scissors": 3}

    wins_against = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    looses_against = {v: k for k, v in wins_against.items()}

    if play == "Y":
        return 3 + scores[oppo]
    if play == "X":
        return scores[wins_against[oppo]]
    return 6 + scores[looses_against[oppo]]


score = 0
for line in records:
    opponent, me = line.split()
    score += result(opponent, me)

print(score)

