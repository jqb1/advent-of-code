with open("./input.txt") as f:
    pairs = [line.rstrip() for line in f]

print(pairs)
counter = 0
for pair in pairs:
    assignment1, assignment2 = pair.split(",")
    range1 = list(map(lambda x: int(x), assignment1.split("-")))
    range2 = list(map(lambda x: int(x), assignment2.split("-")))
    range1[1] += 1
    range2[1] += 1

    section1 = set(range(*range1))
    section2 = set(range(*range2))
    """ task 1 """
    # longer = section1 if len(section1) > len(section2) else section2
    # if longer == section1 | section2:
    #     counter += 1
    """ task 2 """
    if len(section1 | section2) < len(section1) + len(section2):
        counter += 1

print(counter)