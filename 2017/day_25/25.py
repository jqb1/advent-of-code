from collections import defaultdict

from utils import read_input, submit


def solve():
    inp = read_input().split('\n\n')
    state = inp[0].split('\n')[0].split()[-1][:-1]
    steps = int(inp[0].split('\n')[1].split()[-2])
    conditions = {}
    for cond in inp[1:]:
        lines = cond.split('\n')
        cur_s = lines[0][-2]
        conditions[cur_s] = {0: [], 1: []}
        current, write, move, n_state = None, None, None, None
        for line in lines[1:]:
            if "current" in line:
                current = int(line[-2])
            elif "Write" in line:
                write = line[-2]
                conditions[cur_s][current].append(write)
            elif "Move" in line:
                move = line.split()[-1][:-1]
                conditions[cur_s][current].append(move)
            elif "Continue" in line:
                n_state = line[-2]
                conditions[cur_s][current].append(n_state)
    step = 0
    val = 0
    pos = 0
    tape = defaultdict(int)
    while step < steps:
        instr = conditions[state]
        write, move, new_state = instr[tape[pos]]
        tape[pos] = int(write)
        pos += (1 if move == "right" else -1)
        state = new_state
        step += 1
    ans = sum(tape.values())
    submit(ans, 1)


if __name__ == "__main__":
    solve()
