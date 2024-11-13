from collections import deque


def read_input():
    with open("./input.txt") as f:
        lines = [list(map(int, list(line.rstrip()))) for line in f]
    return lines


DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1))


def main():
    octopus_map = read_input()
    max_r, max_c = len(octopus_map) - 1, len(octopus_map[0]) - 1
    flash_count = 0
    # part1
    # for step in range(1, 101):
    # part2
    synchronized = False
    step = 1
    while not synchronized:
        flashed = set()
        to_check = deque([])
        for row in range(max_r + 1):
            for col in range(max_c + 1):
                if (row, col) in flashed:
                    continue
                flashed, to_check, flash = increase_energy(
                    row, col, flashed, octopus_map, to_check, max_r, max_c
                )
                flash_count += flash
        while to_check:
            row_, col_ = to_check.popleft()
            if (row_, col_) in flashed:
                continue
            flashed, to_check, flash = increase_energy(
                row_, col_, flashed, octopus_map, to_check, max_r, max_c
            )
            flash_count += flash
        if len(flashed) == (max_r + 1) * (max_c + 1):
            print("all flashed in step", step)
            synchronized = True
        if step == 100:
            print(flash_count)
        step += 1


def increase_energy(row, col, flashed, octopus_map, to_check, max_r, max_c):
    octopus_map[row][col] += 1
    flash = 0
    if octopus_map[row][col] > 9:
        flashed.add((row, col))
        flash = 1
        octopus_map[row][col] = 0
        for dr, dc in DIRECTIONS:
            if 0 <= row + dr <= max_r and 0 <= col + dc <= max_c:
                to_check.append((row + dr, col + dc))

    return flashed, to_check, flash


if __name__ == "__main__":
    main()
