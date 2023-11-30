import re

with open("./input.txt") as f:
    moves = [line.rstrip() for line in f]
# Test:
# moves = \
# '''
#     [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
#
# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
# '''.splitlines()[1:]

stack_num = int(moves[8][-1])
stacks = {i+1: [] for i in range(stack_num)}

for line in moves:
    if line.startswith(" 1"):
        break
    for stack_key, line_position in zip(stacks.keys(), range(0, len(moves[7]), 4)):
        if len(line) < line_position:
            continue
        crate = line[line_position + 1]
        if crate != ' ':
            stacks[stack_key].append(crate)
for stack in stacks:
    stacks[stack] = stacks[stack][::-1]

print(stacks)
for move in moves:
    if not move.startswith("move"):
        continue
    _num, _from, _to = re.match(r"move (\d+) from (\d+) to (\d+)", move).groups()
    _num, _from, _to = int(_num), int(_from), int(_to)
    print(_num, _from, _to, move)
    # task1
    # for _ in range(_num):
    #     crate = stacks[_from].pop()
    #     stacks[_to].append(crate)
    multi_crates = stacks[_from][-_num:]
    stacks[_from] = stacks[_from][:-_num]
    stacks[_to] += multi_crates

print(stacks)
result = ""
for _, v in stacks.items():
    result += v[-1]
print(result)
