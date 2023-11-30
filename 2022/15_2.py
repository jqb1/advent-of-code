import re


def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


MAX_XY = 4000000

possible_points = set()


# for point check if dist between is bigger than

def main():
    sensors = set()
    distances = set()
    possible_points = set()

    for line in read_input():
        print(line)
        x1, y1, x2, y2 = re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)",
                                  line).groups()
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        distance = abs(x2 - x1) + abs(y2 - y1)
        sensors.add((x1, y1, distance))
        distances.add(distance)

        for cur_dy in range(distance + 1):
            r = distance - cur_dy
            possible_points.add((x1 - r - 1, y1 + cur_dy))
            possible_points.add((x1 + r + 1, y1 + cur_dy))
            possible_points.add((x1 - r - 1, y1 - cur_dy))
            possible_points.add((x1 + r + 1, y1 - cur_dy))

    # if distance is bigger than to any distances (source -> beacon)
    for x, y in possible_points:
        if x < 0 or y < 0 or y > MAX_XY or x > MAX_XY:
            continue
        if check_if_distance_longer(x, y, sensors):
            print('point:', x, y, )
            print(x * 4000000 + y)
            return
        else:
            continue


def check_if_distance_longer(x, y, sensors):
    for sen_x, sen_y, s_dist in sensors:
        cur_dist = abs(x - sen_x) + abs(y - sen_y)
        if cur_dist <= s_dist:
            return False
    return True


if __name__ == "__main__":
    main()
