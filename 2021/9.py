def read_input():
    with open("./input.txt") as f:
        lines = [list(map(int, list(line.rstrip()))) for line in f]
    return lines


DIRECTIONS = (
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
)


def main():
    heightmap = read_input()
    max_row = len(heightmap) - 1
    max_col = len(heightmap[0]) - 1

    risk_lvl = 0
    for row in range(len(heightmap)):
        for col in range(len(heightmap[0])):
            p = heightmap[row][col]
            if all(row + dr in (max_row + 1, -1) or col + dc in (max_col + 1, -1)
                   or heightmap[row + dr][col + dc] > p for dr, dc in DIRECTIONS):
                risk_lvl += p + 1
                print(p)
    print(risk_lvl)


if __name__ == "__main__":
    main()
