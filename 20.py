import re
from collections import defaultdict


def read_input():
    with open("/Users/jkoziol/Downloads/input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines

numbers = list(map(int, read_input()))
num_backup = numbers[:]
idx_to_num = {i: n for i, n in enumerate(numbers)}
num_to_indices = defaultdict(list)

for i, num in enumerate(numbers):
    num_to_indices[num].append(i)
print(numbers)
print("num to idx:", num_to_indices)
print("idx to num:", idx_to_num)

last_idx = len(numbers) - 1

for num in num_backup:
    old_idx = num_to_indices[num].pop(0)
    new_idx = old_idx + num
    if new_idx == 0:
        new_idx = last_idx
    elif new_idx < 0:
        new_idx = new_idx % last_idx
    elif new_idx > last_idx:
        new_idx = new_idx % last_idx
    num_to_indices[num].append(new_idx)
    ch = -1 if new_idx > old_idx else +1
    for i in range(min(old_idx, new_idx), max(old_idx, new_idx) +1):
        if i != old_idx:
            indices = num_to_indices[idx_to_num[i]]
            ind = indices.index(i)
            indices[ind] += ch
    idx_to_num = {i: n for n, indices in num_to_indices.items() for i in indices}

new_numbers = []
for i in range(len(numbers)):
    new_numbers.append(idx_to_num[i])

print(new_numbers)
print(sum((new_numbers[(new_numbers.index(0) + 1000) % len(numbers)],
           new_numbers[(new_numbers.index(0) + 2000) % len(numbers)],
           new_numbers[(new_numbers.index(0) + 3000) % len(numbers)])))