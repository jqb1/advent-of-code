from collections import defaultdict


def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


def solve():
    registers = defaultdict(int)
    inp = read_input()
    max_ever = 0
    for line in inp:
        reg, inst, num, _, *expr = line.split()
        condition = f"{registers[expr[0]]} {expr[1]} {expr[2]}"
        if inst == "inc" and eval(condition):
            registers[reg] += int(num)
        elif inst == "dec" and eval(condition):
            registers[reg] -= int(num)
        max_ever = max(max_ever, registers[reg])
    print(max_ever)


solve()
