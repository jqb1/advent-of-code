from collections import defaultdict
from os import name
from dataclasses import dataclass


def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


name_to_weight = {}
name_to_children = {}


def solve():
    input_ = read_input()
    child_nodes = set()

    for line in input_:
        line = line.split("->")
        name = line[0].split()[0]
        if len(line) > 1:
            children = {name.strip() for name in line[1].split(",")}
            child_nodes.update(children)
            name_to_children[name] = children
        weight = int(line[0].split()[1][1:-1])
        name_to_weight[name] = weight
    root = list(set(name_to_weight.keys()) - child_nodes)[0]

    find_differing_el(root, None)


def calc_weight(node):
    children = name_to_children.get(node)
    if not children:
        return name_to_weight[node]
    s = 0
    for c in children:
        s += calc_weight(c)
    return s + name_to_weight[node]


def find_differing_el(node, diff):
    children = name_to_children.get(node)
    if not children:
        return name_to_weight[node]
    weight_to_n = defaultdict(list)
    for n in name_to_children[node]:
        weight_to_n[calc_weight(n)].append(n)
    if len(weight_to_n) == 1:
        print("answer:", node, name_to_weight[node] + diff)
    for w, nodes in weight_to_n.items():
        if len(nodes) == 1:
            diff = sum(weight_to_n.keys()) - w - w
            find_differing_el(nodes[0], diff)
            break


solve()
