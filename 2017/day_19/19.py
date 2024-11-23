def read_input():
    with open("./input.txt") as f:
        lines = [list(line)[:-1] for line in f]
    return lines


DIRECTIONS = (
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
)
DIR_TO_BACK = {
    (0, 1): (0, -1),
    (0, -1): (0, 1),
    (1, 0): (-1, 0),
    (-1, 0): (1, 0),
}


def solve():
    track = read_input()
    cur_p = 0, track[0].index("|")
    cur_dir = DIRECTIONS[2]
    res = ""
    sc = 1
    while True:
        row, col = cur_p
        dr, dc = cur_dir
        if (
            row + dr >= len(track)
            or row + dr < 0
            or col + dc >= len(track[0])
            or col + dc < 0
            or track[row + dr][col + dc] == " "
        ):
            cur_dir = new_dir(cur_p, track, cur_dir)
            if not cur_dir:
                # p1
                print("p1 result", res + track[row][col])
                # p2
                print("p2 steps", sc)
                return
        if (letter := track[row][col]).isalpha():
            res += letter
            print(letter)
        cur_p = (row + cur_dir[0], col + cur_dir[1])
        sc += 1
        print(track[cur_p[0]][cur_p[1]])


def new_dir(cur_p, track, cur_dir):
    for d in DIRECTIONS:
        if (
            d != cur_dir
            and track[cur_p[0] + d[0]][cur_p[1] + d[1]] != " "
            and d != DIR_TO_BACK[cur_dir]
        ):
            return d


def print_track(track):
    for line in track:
        print(" ".join(line))


solve()
