def solve():
    c = 0
    for i in range(278384, 824795):
        if is_valid(i):
            c += 1
    print(c)


def is_valid(num):
    num_s = str(num)
    same_nr = 0
    prev_d = None
    num_cond = False
    for d in num_s:
        if prev_d and int(prev_d) > int(d):
            return False
        if prev_d and int(prev_d) == int(d):
            same_nr += 1
        elif prev_d and int(prev_d) != int(d):
            if same_nr == 1:
                num_cond = True
            same_nr = 0
        prev_d = d
    return num_cond or same_nr == 1


if __name__ == "__main__":
    solve()
