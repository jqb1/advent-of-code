from collections import defaultdict


def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


def solve():
    inp = read_input()[0].split(",")
    boxes = defaultdict(dict)
    for el in inp:
        if len(sp := el.split("=")) == 2:
            label, focal_len = sp
            box_n = hash_(label)
            boxes[box_n][label] = int(focal_len)
        else:
            label = el.split("-")[0]
            box_n = hash_(label)
            if label in boxes[box_n]:
                del boxes[box_n][label]
            if not boxes[box_n]:
                del boxes[box_n]
    print(boxes)
    res = 0
    for box, lenses in boxes.items():
        for i, focal_l in enumerate(lenses.values()):
            r = (box + 1) * (i + 1) * focal_l
            res += r
    print(res)


def hash_(element):
    cur_val = 0
    for letter in element:
        cur_val += ord(letter)
        cur_val *= 17
        cur_val = cur_val % 256
    return cur_val


solve()
