from collections import defaultdict

from utils import read_input


def solve():
    ws, gs = read_input().rstrip().split('\n\n')
    wires = {ws.split()[0][:-1]: int(ws.split()[1]) for ws in ws.split('\n')}
    all_zs = {line.split()[-1] for line in gs.split('\n') if line.split()[-1][0] == "z"}
    while True:
        for line in gs.split('\n'):
            w1, gate_name, w2, _, w_out = line.split()
            if w1 in wires and w2 in wires:
                wires[w_out] = gate(gate_name, wires[w1], wires[w2])
            if out_val := get_zs(wires, all_zs):
                print("found", out_val)
                return


def get_zs(wires, all_zs):
    zs = {k: v for k, v in wires.items() if k[0] == "z"}
    if not set(zs) == all_zs:
        return 0
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
