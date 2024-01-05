import re
import sympy

def read_input():
    with open("./input.txt") as f:
        lines = [tuple(map(int, re.findall("-?\d+", line))) for line in f]
    return lines


BOUNDS = (200000000000000, 400000000000000)


def solve():
    hail = read_input()
    c = 0
    for i in range(len(hail) - 1):
        stone1 = hail[i]
        coeffs1 = get_coefficients(stone1)
        for j in range(i + 1, len(hail)):
            stone2 = hail[j]
            coeffs2 = get_coefficients(stone2)
            # parallel
            if coeffs1[0] == coeffs2[0]:
                continue
            x, y = get_cross_point(*coeffs1, *coeffs2)
            if BOUNDS[0] <= x <= BOUNDS[1] and BOUNDS[0] <= y <= BOUNDS[1]:
                if crossed_in_past(stone1[0], stone1[3], x) or crossed_in_past(stone2[0], stone2[3], x):
                    continue
                c += 1
    return c


def crossed_in_past(x0, vx, cross_x):
    if vx > 0:
        return cross_x < x0
    else:
        return cross_x > x0


def get_coefficients(stone):
    px, py, pz, vx, vy, vz = stone
    # can be determined by y1-y0/ x1-x0
    a = vy/vx
    # y = ax + b => b = y - ax
    b = py - a*px
    return a, b


def get_cross_point(a1, b1, a2, b2):
    # a1x + b1 = a2x + b2
    # a1x - a2x = b2 - b1
    # x = (b2-b1)/(a1-a2)
    x = (b2 - b1) / (a1 - a2)
    y = a1 * x + b1
    return x, y


p1 = solve()
print(p1)

