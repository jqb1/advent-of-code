from collections import defaultdict
from itertools import chain

from utils import read_input


def solve():
    patterns = {}
    for line in read_input():
        inp_p, out_p = line.split(" => ")
        cur_pat = tuple(map(tuple, inp_p.split("/")))
        out_pat = tuple(map(tuple, out_p.split("/")))
        patterns[cur_pat] = out_pat
        for additional in flip_pat(cur_pat):
            assert additional not in patterns or patterns[additional] == out_pat
            patterns[additional] = out_pat

    i = 0
    image = [list(".#."), list("..#"), list("###")]
    while i < 18:
        sq_size = 2 if len(image) % 2 == 0 else 3
        image = divide_evenly(sq_size, image, patterns)
        for r in image:
            print(r)
        i += 1
        l = list(chain.from_iterable(image))
        print(l.count('#'))


def flip_pat(pat):
    flips = []
    pat = transpose(pat)
    flips.append(pat)
    pat = flip(pat)
    flips.append(pat)
    pat = transpose(pat)
    flips.append(pat)
    pat = flip(pat)
    flips.append(pat)
    pat = transpose(pat)
    flips.append(pat)
    pat = flip(pat)
    flips.append(pat)
    pat = transpose(pat)
    flips.append(pat)
    return flips


def transpose(p):
    return tuple((zip(*p)))


def flip(p):
    return tuple([r for r in p[::-1]])


def divide_evenly(sq_size, grid, patterns):
    squares = defaultdict(list)
    if len(grid) == 1:
        grid = grid[0]
    for tr in range(len(grid)):
        for tc in range(len(grid[0])):
            sq_r, r = divmod(tr, sq_size)
            sq_c = tc // sq_size
            if r >= len(squares[(sq_r, sq_c)]):
                squares[(sq_r, sq_c)].append([])
            squares[(sq_r, sq_c)][r].append(grid[tr][tc])
    new_img = []
    for sqk, sq in squares.items():
        n_sq = patterns[tuple(map(tuple, sq))]
        squares[sqk] = n_sq
    size_in_sq = len(grid) // sq_size
    squares = list(squares.values())
    sq_size = len(squares[0])
    for si in range(0, len(squares), size_in_sq):
        for row in range(sq_size):
            new_row = []
            for s in range(si, si+size_in_sq):
                new_row.extend(squares[s][row])
            new_img.append(new_row)
    return new_img


if __name__ == "__main__":
    solve()
    # s = """
    # .#.
    # ..#
    # ###
    # """
    # p = list(map(tuple, s.split()))
    # match_pat(p, {})
