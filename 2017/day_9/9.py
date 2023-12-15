
def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


def solve():
    inp = read_input()[0]
    nest_lvl = 0
    score = 0
    garbage_on = False
    cancel = False
    garbage_c = 0
    for char in inp:
        if cancel:
            cancel = False
            continue
        if char == ">" and garbage_on:
            garbage_on = False
        if char == "!":
            cancel = True
        if garbage_on:
            if char not in {"!", ">"}:
                garbage_c += 1
            continue
        elif char == "{":
            nest_lvl += 1
        elif char == "}":
            score += nest_lvl
            nest_lvl -= 1
        elif char == "<":
            garbage_on = True

    print(garbage_c)



solve()