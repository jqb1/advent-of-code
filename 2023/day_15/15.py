import re
from collections import defaultdict


def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


def solve():
    inp = read_input()[0].split(",")
    boxes = defaultdict(list)
    label_to_focal = {}
    for el in inp:
        if len(sp := el.split("=")) == 2:
            label, focal_len = sp
            label_to_focal[label] = int(focal_len)
            box_n = hash_(label)
            if label not in boxes[box_n]:
                boxes[box_n].append(label)
        else:
            label = el.split("-")[0]
            box_n = hash_(label)
            if label in boxes[box_n]:
                boxes[box_n].remove(label)
            if not boxes[box_n]:
                del boxes[box_n]
    print(boxes)
    print(label_to_focal)
    res = 0
    for box, lenses in boxes.items():
        for i, lens in enumerate(lenses):
            r = (box + 1) * (i + 1) * label_to_focal[lens]
            res += r
    print(res)




def hash_(element):
    cur_val = 0
    for letter in element:
        cur_val += ord(letter)
        cur_val *= 17
        cur_val = cur_val % 256
    return cur_val


# print(hash_("cm"))
solve()