def read_input():
    with open("/Users/jkoziol/Downloads/input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


def add_rocks(lines, cave):
    max_row = 0
    for line in lines:
        prev = None
        for i in range(0, len(line), 2):
            col, row = line[i], line[i + 1]
            if row > max_row:
                max_row = row
            if prev:
                prev_r, prev_c = prev
                if prev_r == row:
                    cc = -1 if col > prev_c else 1
                    current_c = col
                    for _ in range(abs(prev_c - col) + 1):
                        cave[row][current_c] = "#"
                        current_c += cc
                else:
                    cr = -1 if row > prev_r else 1
                    current_r = row
                    for _ in range(abs(prev_r - row) + 1):
                        cave[current_r][col] = "#"
                        current_r += cr
                prev = (row, col)
            else:
                prev = (row, col)
    return max_row


def draw_sand(cave, max_row):
    # Sand keeps moving as long as it is able to do so, at each step
    # trying to move down, then down-left, then down-right.
    # If all three possible destinations are blocked,
    # the unit of sand comes to rest and no longer moves,
    # at which point the next unit of sand is created back at the source.

    row = 0
    col = 500
    stop = False
    while not stop:
        if row > max_row:
            return True
        if cave[row + 1][col] == '.':
            row += 1
        elif cave[row + 1][col] == '#' or cave[row + 1][col] == "o":
            if cave[row + 1][col - 1] == '.':
                col -= 1
                continue
            elif cave[row + 1][col + 1] == '.':
                col += 1
                continue
            else:
                stop = True
    if (row, col) == (0, 500):
        return True
    cave[row][col] = "o"
    return False


#     return False

def main():
    lines = [tuple(map(int, line.replace(" -> ", ",").split(','))) for line in read_input()]

    cave = [['.'] * 1000 for _ in range(1000)]
    cave[0][500] = "+"

    max_row = add_rocks(lines, cave)

    for c_ in range(1000):
        cave[max_row+2][c_] = "#"

    fin = False
    count = 0
    while not fin:
        fin = draw_sand(cave, max_row + 2)
        count += 1

    print(count)

if __name__ == "__main__":
    main()

# x represents distance to the right and y represents distance down
