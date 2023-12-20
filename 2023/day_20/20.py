import math
from collections import deque


def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


def solve():
    inp = read_input()
    flip_flops = {}
    conjunctions = {}
    broadcaster = []

    # hardcoded from input
    # "zh" node is the last one before ending node "rx"
    zh_pointers = {"jt", "kb", "ks", "sx"}
    cycle_counters = {k: 0 for k in zh_pointers}
    for line in inp:
        module, dest_modules = line.split("->")
        dest_modules = [m.strip() for m in dest_modules.split(",")]
        m_type, m_name = module[0], module[1:].rstrip()
        if m_type == "%":
            flip_flops[m_name] = {"state": "off", "outputs": dest_modules}
        elif m_type == "&":
            conjunctions[m_name] = {"inputs": {}, "outputs": dest_modules}
        else:
            broadcaster = dest_modules

    discover_conjunction_inputs(flip_flops, conjunctions)
    print("ff: ", flip_flops)
    print("cnj: ", conjunctions)
    low_c = 0
    high_c = 0
    for i in range(1, 100000):
        # target, signal, source
        q = deque([("broadcaster", "low", "button")])
        print(f"----------press {i + 1}------------")
        while q:
            receiver, signal, sender = q.popleft()
            if receiver == "zh" and sender in zh_pointers and signal == "high":
                cycle_counters[sender] = i
            # only if all send high to zh it'll output "low"
            if all(v != 0 for v in cycle_counters.values()):
                print("part2:", math.lcm(*cycle_counters.values()))
                return

            if signal == "low":
                low_c += 1
            else:
                high_c += 1
            if receiver == "broadcaster":
                new_targets = broadcaster
                out_signals = prepare_out_signals(source=receiver, signal=signal, outputs=new_targets)
            elif receiver in flip_flops:
                out_signal = handle_ff_signal(signal, flip_flops[receiver])
                if not out_signal:
                    continue
                out_signals = prepare_out_signals(source=receiver, signal=out_signal,
                                                  outputs=flip_flops[receiver]["outputs"])
            elif receiver not in conjunctions:
                if receiver == "rx" and signal == "low":
                    print("part2:", i)
                    return
                continue
            else:
                out_signal = handle_conj_signal(signal, conjunctions[receiver], sender)
                out_signals = prepare_out_signals(source=receiver, signal=out_signal,
                                                  outputs=conjunctions[receiver]["outputs"])
            q.extend(out_signals)
    print(low_c, high_c, f"res:{low_c*high_c}")


def handle_ff_signal(signal, ff):
    if signal == "high":
        return
    # flip state
    ff["state"] = "on" if ff["state"] == "off" else "off"

    out_signal = "high" if ff["state"] == "on" else "low"
    return out_signal


def handle_conj_signal(signal, conj, sender):
    conj["inputs"][sender] = signal
    if all(v == "high" for v in conj["inputs"].values()):
        return "low"
    return "high"


def prepare_out_signals(source, signal, outputs):
    # (target, signal, sender) format
    return [(o, signal, source) for o in outputs]


def discover_conjunction_inputs(flip_flops, conjunctions):
    for ff_name, ff in flip_flops.items():
        for o in ff["outputs"]:
            if o in conjunctions:
                conjunctions[o]["inputs"][ff_name] = "low"


solve()
