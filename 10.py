def read_input():
    with open("/Users/jkoziol/Downloads/input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


X = 1  # During the first cycle, X is 1
cycle_now = 0
cycles_strngs = (20, 60, 100, 140, 180, 220)
signal_strengths = []

screen = ""
line_len = 0
for line in read_input():
    line = line.split()
    print(line)
    cycles_td = 1 if line[0] == "noop" else 2
    for cycle in range(cycles_td):
        if any(pixel == cycle_now % 40 for pixel in (X-1, X, X+1,)):
            screen += "#"
        else:
            screen += "."
        line_len += 1
        if cycle_now in cycles_strngs:
            signal_strengths.append(cycle_now * X)

        if line_len == 40:
            screen += "\n"
            line_len = 0
        if line[0] == "noop":
            cycle_now += 1
            continue
        elif line[0] == "addx":
            cycle_now += 1
            # check
            if cycle == 1:
                X += int(line[1])

print(signal_strengths)
print(sum(signal_strengths))
# the sprite is 3 pixels wide, and the X register sets the horizontal position of the middle of that sprite.
print(screen)
