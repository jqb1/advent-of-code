import re
from collections import defaultdict, deque


def read_input():
    with open("/Users/jkoziol/Downloads/input.txt") as f:
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
    # q = deque([(current_valive, 30, 0, tuple(), current_valve)])
    distances = search_flow_rate(tunnels, valves)
    print(distances)
    bfs_max_pressure(distances, valves)


#  1547 is to high 1463, too high
def search_flow_rate(tunnels, valves):
    distances = defaultdict(dict)

    # store cost of traversing to all the non zero valves
    for rval in valves:
        q = deque([(rval, 0)])
        visited = {rval}
        while q:
            valve, distance = q.popleft()
            for neighbor in tunnels[valve]:
                if neighbor in visited:
                    continue
                if valves[neighbor]:
                    distances[rval][neighbor] = distance + 1
                q.append((neighbor, distance + 1))
                visited.add(neighbor)
    return distances


def bfs_max_pressure(distances, valves):
    minutes, turned = 30, tuple()
    q = deque([('AA', 30, turned, 0)])
    cur_max = 0
    while q:
        valve, minutes, turned, pres = q.popleft()
        print(valve, minutes, pres, cur_max, turned)
        if minutes == 0:
            print(minutes, turned, pres, cur_max)
            if pres > cur_max:
                cur_max = pres
            continue
        if valve not in turned and minutes - 1 > 0 and valve !='AA':
            minutes -= 1
            # pressure that will be produced from now up until the end of 30min time
            pres += minutes * valves[valve]
            if pres > cur_max:
                cur_max = pres
            turned += (valve, )

        for neighbor, cost in distances[valve].items():
            if neighbor not in turned:
                if minutes - cost > 0:
                    q.append((neighbor, minutes - cost, turned, pres))
                else:
                    continue

if __name__ == '__main__':
    main()
