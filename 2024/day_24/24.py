from collections import defaultdict
from functools import cache

from utils import read_input, ints


def solve():
    ws, gs = read_input().rstrip().split('\n\n')
    wires = {ws.split()[0][:-1]: int(ws.split()[1]) for ws in ws.split('\n')}
    for line in gs.split('\n'):
        if 'x' in line and 'y' in line and "XOR" in line:
            int_c = ints(line)[0], ints(line)[1]
            if len(set(int_c)) > 1:
                print("different")
            print(line)
    # 4 out_wires swaps needed
    # which wires need to be swapped to get sum of 2 binary numbers
    # x, y = 11, 15

    # x_wires = num_to_bin_wires('x', x)
    # y_wires = num_to_bin_wires('y', y)
    # print(num_to_bin_wires('z', 27))

    for x in range(2097100, 2097300):
        for y in range(1, 10000):
            # this helped me find the wrong bits by hand and looking into the input to reverse engineer what's wrong
            # I'll update it later to detect it automatically
            x_wires = num_to_bin_wires('x', x)
            y_wires = num_to_bin_wires('y', y)

            out_z_int = system(gs, x_wires | y_wires)
            expected = num_to_bin_wires('z', x+y)
            actual = num_to_bin_wires('z', out_z_int)
            print(f"\nadding: {x},{y}")
            print('          ', x_wires)
            print('          ', y_wires)
            print("should be:", expected, "in dec:", x+y)
            print("is:       ", actual, "in dec:", out_z_int)
            if actual != expected:
                print("not equal")
                return


def num_to_bin_wires(wire_name, num):
    num_bin = f'{num:045b}'
    return {f'{wire_name}{i:02d}': int(n) for i, n in enumerate(num_bin[::-1])}


def system(gs, wires):
    all_zs = {line.split()[-1] for line in gs.split('\n') if line.split()[-1][0] == "z"}
    while True:
        for line in gs.split('\n'):
            w1, gate_name, w2, _, w_out = line.split()
            if w1 in wires and w2 in wires:
                wires[w_out] = gate(gate_name, wires[w1], wires[w2])
            if out_val := get_zs(wires, all_zs):
                print("found", out_val)
                return out_val


def get_zs(wires, all_zs):
    zs = {k: v for k, v in wires.items() if k[0] == "z"}
    if not set(zs) == all_zs:
        return None
    out = []
    for k in sorted(zs)[::-1]:
        out.append(str(zs[k]))
    return int(''.join(out), 2) if out else 0


def gate(name, w1, w2):
    match name:
        case "AND":
            return w1 & w2
        case "OR":
            return w1 | w2
        case "XOR":
            return w1 ^ w2


if __name__ == "__main__":
    solve()
