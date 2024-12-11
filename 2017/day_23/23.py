import asyncio
from collections import defaultdict

from utils import read_input, submit


def solve():
    instructions = [line.rstrip().split() for line in read_input().split('\n')]
    t1 = start_program(instructions, 0)
    print("finished", t1)


def start_program(instructions, prog_num):
    pos = 0
    regs = defaultdict(int)
    # Each program also has its own program ID (one 0 and the other 1); the register p should begin with this value.
    regs["a"] = 1
    cnt = 0

    c = 0
    last_p = []
    while pos < len(instructions):
        print(f"p{prog_num} pos{pos}")
        print([f"{k}={v}" for k, v in regs.items()])
        inst, *args = instructions[pos]
        match inst:
            case "set":
                regs[args[0]] = (
                    int(args[1])
                    if args[1].lstrip("-").isnumeric()
                    else int(regs[args[1]])
                )
            case "sub":
                regs[args[0]] -= (
                    int(args[1])
                    if args[1].lstrip("-").isnumeric()
                    else int(regs[args[1]])
                )
            case "mul":
                regs[args[0]] *= (
                    int(args[1])
                    if args[1].lstrip("-").isnumeric()
                    else int(regs[args[1]])
                )
                cnt += 1
            case "jnz":
                arg = (
                    int(args[0])
                    if args[0].lstrip("-").isnumeric()
                    else int(regs[args[0]])
                )
                # if pos == 19 and c == 0:
                #     c += 1
                #     regs["e"] += abs(regs["g"])
                #     regs["g"] = 0
                # elif pos == 23:
                #     regs["d"] += abs(regs["g"])
                #     regs["g"] = 0
                if arg != 0:
                    pos += (
                        int(args[1])
                        if args[1].lstrip("-").isnumeric()
                        else int(regs[args[1]])
                    )
                    continue

        pos += 1
    print(cnt)
    return regs["h"]


if __name__ == "__main__":
    solve()
