import re
import sympy


def read_input():
    with open("./input.txt") as f:
        lines = [tuple(map(int, re.findall("-?\d+", line))) for line in f]
    return lines


def solve():
    hail_stones = read_input()[:3]
    equations = []
    x, y, z, dx, dy, dz, t1, t2, t3 = sympy.symbols("x,y,z,dx,dy,dz,t1,t2,t3")
    for stone, dt in zip(hail_stones, [t1, t2, t3]):
        x0, y0, z0, vx, vy, vz = stone
        # x axis
        equations.append(sympy.Eq(x + dx * dt, x0 + vx * dt))
        # y axis
        equations.append(sympy.Eq(y + dy * dt, y0 + vy * dt))
        # z axis
        equations.append(sympy.Eq(z + dz * dt, z0 + vz * dt))
    # t == 0, find x,y,z
    res = sympy.solve(equations, (x, y, z, dx, dy, dz, t1, t2, t3))[0]
    print(sum(res[:3]))


solve()
