from collections import defaultdict
import asyncio


def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip().split() for line in f]
    return lines


q0, q1 = asyncio.Queue(), asyncio.Queue()
snd_cnt = 0


async def solve():
    instructions = read_input()
    t1 = asyncio.create_task(start_program(instructions, 0))
    t2 = asyncio.create_task(start_program(instructions, 1))
    await asyncio.gather(t1, t2)
    print("finished", snd_cnt)


async def start_program(instructions, prog_num):
    global snd_cnt

    pos = 0
    rcv_reg = None
    regs = defaultdict(int)
    # Each program also has its own program ID (one 0 and the other 1); the register p should begin with this value.
    regs["p"] = prog_num
    while pos < len(instructions):
        print(f"p{prog_num} pos{pos}")
        inst, *args = instructions[pos]
        match inst:
            case "set":
                regs[args[0]] = (
                    int(args[1])
                    if args[1].lstrip("-").isnumeric()
                    else int(regs[args[1]])
                )
            case "add":
                regs[args[0]] += (
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
            case "mod":
                regs[args[0]] %= (
                    int(args[1])
                    if args[1].lstrip("-").isnumeric()
                    else int(regs[args[1]])
                )
            case "snd":
                snd_val = int(regs[args[0]])
                await q1.put(snd_val) if prog_num == 0 else await q0.put(snd_val)
                print(f"send p{prog_num}")
                if prog_num == 1:
                    snd_cnt += 1
            case "rcv":
                # part 1
                # arg = int(args[0]) if args[0].lstrip("-").isnumeric() else int(regs[args[0]])
                print(f"{inst} {args[0]} p{prog_num}")
                if q0.empty() and q1.empty():
                    print("answer", snd_cnt)
                    # if deadlock (expected) send exit message to the other task and return
                    await q1.put("exit") if prog_num == 0 else await q0.put("exit")
                    return

                val = await q0.get() if prog_num == 0 else await q1.get()
                if val == "exit":
                    return
                regs[args[0]] = val

            case "jgz":
                arg = (
                    int(args[0])
                    if args[0].lstrip("-").isnumeric()
                    else int(regs[args[0]])
                )
                if arg > 0:
                    pos += (
                        int(args[1])
                        if args[1].lstrip("-").isnumeric()
                        else int(regs[args[1]])
                    )
                    continue
        pos += 1
    return snd_cnt


asyncio.run(solve())
