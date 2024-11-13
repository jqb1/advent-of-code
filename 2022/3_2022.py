with open("./input.txt") as f:
    rucksacks = [line.rstrip() for line in f]


priorities = {
    letter: prio
    for letter, prio in zip(
        [chr(l) for l in range(ord("a"), ord("z") + 1)], range(1, 27)
    )
}
priorities_big = {
    letter: prio
    for letter, prio in zip(
        [chr(l) for l in range(ord("A"), ord("Z") + 1)], range(27, 53)
    )
}
priorities.update(priorities_big)

test = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]

sum = 0
""" part 1"""
# for rucksack in rucksacks:
#     compart_1 = set(rucksack[:len(rucksack)//2])
#     compart_2 = set(rucksack[len(rucksack)//2:])
#     letter = list(compart_1.intersection(compart_2))[0]
#     sum += priorities[letter]
""" part 2"""
for common_letter in [
    set(rucksacks[idx]) & set(rucksacks[idx + 1]) & set(rucksacks[idx + 2])
    for idx in list(range(0, len(rucksacks), 3))
]:
    sum += priorities[list(common_letter)[0]]

print(sum)
