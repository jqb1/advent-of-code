import re


def read_input():
    with open("/Users/jkoziol/Downloads/input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


no_beacon = set()
beacons = set()

ROW = 2000000
MAX_XY = 20

def main():
    lines = read_input()
    for line in read_input():
        x1, y1, x2, y2 = re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)",
                                  line).groups()
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        beacons.add((x2, y2))
        distance = abs(x2 - x1) + abs(y2 - y1)

        if y1 + distance < ROW or y1 - distance > ROW:
            continue

        dist_y = abs(ROW - y1)
        # for cur_dy in range(distance+1):
        r = distance - dist_y
        # if y1 + cur_dy > ROW or y1 - cur_dy < ROW:
        #     break
        print(r)
        for dx in range(r+1):
            if y1 + dist_y == ROW:
                no_beacon.add((x1 + dx, y1 + dist_y))
                no_beacon.add((x1 - dx, y1 + dist_y))
            elif y1 - dist_y == ROW:
                no_beacon.add((x1 - dx, y1 - dist_y))
                no_beacon.add((x1 + dx, y1 - dist_y))

    # print(no_beacon)
    # for x_, y_ in sorted(no_beacon):
    #     if y_ == 10 and not (x_, y_) in beacons:
    #         print(x_, y_)
    print(sum(1 if y == ROW and not (x, y) in beacons else 0 for x, y in no_beacon))

    # for y in range(20):
    #     for x in range(20):
    #         if (x, y) not in


if __name__ == "__main__":
    main()
