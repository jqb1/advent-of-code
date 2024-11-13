import math
import operator
import re
from collections import deque


def read_input():
    with open("./input.txt") as f:
        lines = f.read()
    return lines


def solve():
    workflows_inp, parts = read_input().split("\n\n")
    workflows_inp, parts = workflows_inp.split("\n"), parts.split("\n")
    parts = [parse_part(p) for p in parts]
    print(parts)
    workflows = {}
    accepted = []
    rejected = []
    for workflow in workflows_inp:
        name, conditions = parse_workflow(workflow)
        workflows[name] = conditions

    for part in parts:
        w_name = "in"
        while w_name:
            res = process_part(part, workflows[w_name])
            if res == "A":
                accepted.append(part)
                w_name = None
            elif res == "R":
                rejected.append(part)
                w_name = None
            else:
                w_name = res
    # part 1
    print(sum(sum(a.values()) for a in accepted))

    # part 2
    # bfs accepted paths
    possible_paths = explore_possible_paths(workflows)
    #                   x       m      a      s
    # max possible is [4000 * 4000 * 4000 * 4000]
    # reduce it by exploring each path
    s = 0
    ranges = []
    for path in possible_paths:
        path, conds = path
        print(path, conds)
        range_ = calculate_path(conds)
        ranges.append(range_)
        s += math.prod(v[1] - v[0] + 1 for v in range_.values())
    print("result:", s)


def calculate_path(conditions):
    # closed range
    possible_range = [1, 4000]
    ranges = {k: possible_range[:] for k in ("x", "m", "a", "s")}
    for condition in conditions:
        tar, op, val = condition
        val = int(val)
        if op == ">":
            ranges[tar][0] = val + 1
        elif op == ">=":
            ranges[tar][0] = val
        elif op == "<":
            ranges[tar][1] = val - 1
        elif op == "<=":
            ranges[tar][1] = val
    return ranges


def split_condition(condition):
    return tuple(re.split("([<>])", condition))


def process_part(part, workflow):
    operators = {">": operator.gt, "<": operator.lt}
    for rule in workflow:
        rule = rule.split(":")
        if len(rule) == 1:
            return rule[0]
        condition, result = rule

        left, op, right = split_condition(condition)
        if operators[op](part[left], int(right)):
            return result


def parse_workflow(workflow):
    name, conditions = workflow.split("{")
    conditions = conditions[:-1].split(",")
    return name, conditions


def explore_possible_paths(workflows):
    q = deque([(" in", [])])
    accepted_paths = []
    seen = set()

    while q:
        path, conditions = q.popleft()
        cur = path.split()[-1]
        if cur == "A":
            accepted_paths.append((path, conditions))
            continue
        elif cur == "R":
            continue
        if (cur, tuple(conditions)) in seen:
            continue
        seen.add((cur, tuple(conditions)))

        negated_conditions = []
        for rule in workflows[cur][:-1]:
            condition, result = rule.split(":")
            condition = split_condition(condition)
            q.append(
                (f"{path} {result}", conditions + negated_conditions + [condition])
            )
            negated_conditions.append(negate_condition(*condition))

        # path when none of conditions matched
        q.append((f"{path} {workflows[cur][-1]}", conditions + negated_conditions))
    return accepted_paths


def negate_condition(a, op, b):
    if op == ">":
        return a, "<=", b
    return a, ">=", b


def parse_part(part):
    output = {}
    part = part[1:-1]
    for category in part.split(","):
        k, val = category.split("=")
        output[k] = int(val)
    return output


solve()
