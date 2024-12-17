from utils import submit, read_input


def solve():
    lines = read_input().split("\n\n")
    regs = {}

    for line in lines[0].split("\n"):
        if "A:" in line:
            regs["A"] = int(line.split()[-1])
        elif "B:" in line:
            regs["B"] = int(line.split()[-1])
        elif "C" in line:
            regs["C"] = int(line.split()[-1])
        print(line)
    program = lines[1].split()[1].split(",")

    out = run_program(regs["A"], program)
    print(",".join(out))


def run_program(pos_a, program):
    regs = {
        "A": pos_a,
        "B": 0,
        "C": 0,
    }
    pos = 0
    ans = []
    while pos < len(program):
        instr = program[pos]
        if pos + 1 > len(program):
            break
        operand = program[pos + 1]
        # operand after, opcode == instr number
        match instr:
            # adv
            case "0":
                regs["A"] = regs["A"] // 2 ** (get_combo(regs, operand))
            case "1":
                regs["B"] = regs["B"] ^ int(operand)
            case "2":
                regs["B"] = get_combo(regs, operand) % 8
            case "3":
                # jnz
                if regs["A"] != 0:
                    pos = int(operand)
                    continue
            case "4":
                regs["B"] = regs["B"] ^ regs["C"]
            case "5":
                x = get_combo(regs, operand) % 8
                ans.append(str(x))
            case "6":
                regs["B"] = regs["A"] // 2 ** get_combo(regs, operand)
            case "7":
                regs["C"] = regs["A"] // 2 ** get_combo(regs, operand)
        pos += 2
    return ans


def get_combo(regs, opc):
    return {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": regs["A"],
        "5": regs["B"],
        "6": regs["C"],
        "7": None,
    }[opc]


if __name__ == "__main__":
    solve()
