def read_input():
    with open("/Users/jkoziol/Downloads/input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


numbers = list(map(int, read_input()))
print(numbers)

numbers = [(i, num*811589153) for i, num in enumerate(numbers)]
numbers_cpy = numbers[:]

print(numbers)
size = len(numbers) - 1
for _ in range(10):
    for i, n in numbers_cpy:
        if n == 0:
            continue
        idx = numbers.index((i, n))
        numbers.insert((idx + n) % size, numbers.pop(idx))

new_numbers = [n for _, n in numbers]

print(new_numbers)
print(new_numbers[(new_numbers.index(0) + 1000) % len(numbers)])
print(new_numbers[(new_numbers.index(0) + 2000) % len(numbers)])
print(new_numbers[(new_numbers.index(0) + 3000) % len(numbers)])
print(sum((new_numbers[(new_numbers.index(0) + 1000) % len(numbers)],
           new_numbers[(new_numbers.index(0) + 2000) % len(numbers)],
           new_numbers[(new_numbers.index(0) + 3000) % len(numbers)])))