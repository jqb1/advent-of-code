import re
from collections import defaultdict, deque


def read_input():
    with open("/Users/jkoziol/Downloads/input_t.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


def read_reports(reports):
    valves = defaultdict(int)
    leads_to = defaultdict(list)
    first = None
    nonzero = set()
    for num, line in enumerate(reports):
        valve, flowrate, leads_ = re.match(r"Valve (\w\w) has flow rate=(\d+); tunnels* leads* to valves* (.+)",
                                           line).groups()
        if num == 0:
            first = valve
        valves[valve] = int(flowrate)
        if int(flowrate):
            nonzero.add(valve)
        leads_to[valve] = leads_.split(", ")
    return valves, leads_to, first, nonzero


def main():
    # print(read_input())

    minutes = 30
    valves, tunnels, current_valve, nonzero = read_reports(read_input())
    open_valves = []
    print('valves', valves)
    print('tunnels', tunnels)
    q = deque([(current_valve, 30, 0, tuple(), current_valve)])
    search_flow_rate(q, tunnels, valves, nonzero)

#  1547 is to high 1463, too high

def search_flow_rate(q, tunnels, valves, nonzero):
    s = set()
    paths = set()
    max_pres = 0
    only_turned = False
    while q:
        current_valve, minutes, current_pres, turned, path = q.popleft()
        # if path in paths:
        #     continue
        # if current_pres < max_pres//2:
        #     continue
        print(current_valve, minutes, current_pres, max_pres, turned, path)
        if minutes == 0 or set(turned) == nonzero:
            # s.add(current_pres)
            print(current_valve, minutes, current_pres, max_pres, turned, path)

        if current_valve in nonzero and minutes - 1 >= 0 and current_valve not in turned:
            # if not (current_valve == "CC" and minutes == 27):
                turned += (current_valve, )
                minutes -= 1
                current_pres += minutes * valves[current_valve]  # pressure that it'll generate
                if current_pres > max_pres:
                    max_pres = current_pres

        for n in tunnels[current_valve]:
            q.append((n, minutes - 1, current_pres, turned, path + f"/{n}"))

    print(s)


if __name__ == '__main__':
    main()
