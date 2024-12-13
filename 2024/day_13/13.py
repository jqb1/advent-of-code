from utils import read_input, ints

def solve():
    buttons = read_input().split('\n\n')
    ans = 0

    prizes = {}
    for but_set in buttons:
        b, a, prize = None, None, None
        for line in but_set.split("\n"):
            if "B:" in line:
                b = ints(line)
            elif "A:" in line:
                a = ints(line)
            else:
                prize = ints(line)
                prize = prize[0], prize[1]
        prizes[prize] = (a, b)
    a_cost, b_cost = 3, 1
    for prize, ab in prizes.items():
        a, b = ab
        if sol := find_solution(a[0], a[1], b[0], b[1], prize[0], prize[1]):
            a_press, b_press = sol
            cost = a_press * a_cost + b_press * b_cost
            ans += cost
    print(ans)


def solve_p2():
    buttons = read_input().split('\n\n')
    ans = 0

    prizes = {}
    for but_set in buttons:
        b, a, prize = None, None, None
        for line in but_set.split("\n"):
            if "B:" in line:
                b = ints(line)
            elif "A:" in line:
                a = ints(line)
            else:
                prize = ints(line)
                prize = 10000000000000 + prize[0], 10000000000000 + prize[1]
        prizes[prize] = (a, b)
    a_cost, b_cost = 3, 1
    for prize, ab in prizes.items():
        a, b = ab
        if sol := find_solution(a[0], a[1], b[0], b[1], prize[0], prize[1]):
            a_press, b_press = sol
            cost = a_press * a_cost + b_press * b_cost
            ans += cost
    print(ans)


def find_solution(ax, ay, bx, by, px, py):
    """
    determine i and j from 2 equations:
    ax*i + bx*j = px
    ay*i + by*j = py
    """
    i = (-bx * py + by * px) / (ax * by - ay * bx)
    j = (ax * py - ay * px) / (ax * by - ay * bx)
    if not (i.is_integer() and j.is_integer()):
        return
    return int(i), int(j)


if __name__ == "__main__":
    solve()
    solve_p2()
