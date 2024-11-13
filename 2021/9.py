from collections import deque


def read_input():
    with open("./input.txt") as f:
        lines = [list(map(int, list(line.rstrip()))) for line in f]
    return lines


DIRECTIONS = (
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
)


def main():
    heightmap = read_input()
    max_row = len(heightmap) - 1
    max_col = len(heightmap[0]) - 1

    basin_sizes = []
    seen = set()
    risk_lvl = 0
    for row in range(len(heightmap)):
        for col in range(len(heightmap[0])):
            # /part 2/
            size, seen = explore_basin(heightmap, (row, col), seen, max_row, max_col)
            if size > 0:
                basin_sizes.append(size)
            # /part1/
            # p = heightmap[row][col]
            # if all(row + dr in (max_row + 1, -1) or col + dc in (max_col + 1, -1)
            #        or heightmap[row + dr][col + dc] > p for dr, dc in DIRECTIONS):
            #     risk_lvl += p + 1
            #     print(p)
    assert len(seen) == len(heightmap) * len(heightmap[0])
    print(risk_lvl)
    print(basin_sizes)
    basin_sizes = sorted(basin_sizes)
    print(basin_sizes)
    print(basin_sizes[-3] * basin_sizes[-2] * basin_sizes[-1])


def explore_basin(heightmap, point, seen, max_row, max_col):
    q = deque((point,))
    size = 0
    basin = set()
    while q:
        curr_point = q.popleft()
        if curr_point in seen:
            continue
        seen.add(curr_point)
        curr_row, curr_col = curr_point
        curr_h = heightmap[curr_row][curr_col]
        if curr_h == 9:
            continue
        # check neighbors
        size += 1
        basin.add(curr_point)
        for dr, dc in DIRECTIONS:
            if (
                curr_row + dr not in (max_row + 1, -1)
                and curr_col + dc not in (max_col + 1, -1)
                and heightmap[curr_row + dr][curr_col + dc] < 9
                and (curr_row + dr, curr_col + dc) not in seen
            ):
                q.append((curr_row + dr, curr_col + dc))
    if size > 50:
        for row in range(max_row + 1):
            print(
                "  ".join(
                    [
                        f"\033[92m{heightmap[row][col]}\033[0m"
                        if (row, col) in basin
                        else f"{heightmap[row][col]}"
                        for col in range(max_col + 1)
                    ]
                )
            )
        print(point, size)
        print(basin)

    return size, seen


if __name__ == "__main__":
    main()
