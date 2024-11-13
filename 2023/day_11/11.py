from collections import deque


def read_input():
    with open("./input.txt") as f:
        lines = [[ch for ch in line.rstrip()] for line in f]
    return lines


def solve():
    img = read_input()
    galaxy_cords = expand(img)
    print("galaxy cords")
    # for each pair of galaxies
    s = 0
    for i in range(len(galaxy_cords)):
        for j in range(i + 1, len(galaxy_cords)):
            print(galaxy_cords[i], galaxy_cords[j])
            min_dis = distance(galaxy_cords[i], galaxy_cords[j], img)
            print(min_dis)
            s += min_dis
    print(s)


DIRECTIONS = {(0, 1), (0, -1), (1, 0), (-1, 0)}


def distance(gal1, gal2, img):
    return abs(gal1[0] - gal2[0]) + abs(gal1[1] - gal2[1])


def expand(img):
    initial_galaxy_cords = [
        (i, j) for i in range(len(img)) for j in range(len(img[0])) if img[i][j] == "#"
    ]
    current_galaxy_cords = initial_galaxy_cords[:]

    for i, col in enumerate(zip(*img)):
        if set(col) == {"."}:
            print("col", i)
            for gi, cord in enumerate(initial_galaxy_cords):
                if cord[1] > i:
                    cur_i, cur_j = current_galaxy_cords[gi]
                    current_galaxy_cords[gi] = (cur_i, cur_j + 999999)
    for i, row in enumerate(img):
        if set(row) == {"."}:
            print("row", i)
            for gi, cord in enumerate(initial_galaxy_cords):
                if cord[0] > i:
                    cur_i, cur_j = current_galaxy_cords[gi]
                    current_galaxy_cords[gi] = (cur_i + 999999, cur_j)
    return current_galaxy_cords


solve()
