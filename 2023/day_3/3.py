def read_input():
    with open("./input.txt") as f:
        lines = [[ch for ch in line.rstrip()] for line in f]
    return lines


def solve():
    input_ = read_input()
    adjacent_list = [
        (1, -1),
        (1, 0),
        (1, 1),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
    ]

    points = {}
    symbols = set()
    for i in range(len(input_)):
        for j in range(len(input_[0])):
            points[(i, j)] = input_[i][j]
            if not input_[i][j].isdigit() and input_[i][j] != ".":
                symbols.add(input_[i][j])
    valid_points = []
    part_numbers_cords = {}

    num_id = 0
    for i, row in enumerate(input_):
        is_valid = False
        num = ""
        cords = []
        for j, el in enumerate(row):
            if el.isnumeric():
                num += el
                cords.append((i, j))
                if not is_valid:
                    is_valid = any(
                        points.get((i + di, j + dj), 0) in symbols
                        for di, dj in adjacent_list
                    )

            elif not el.isnumeric() and is_valid and num != "":
                num_id += 1
                valid_points.append(int(num))
                for cord in cords:
                    part_numbers_cords[cord] = (int(num), num_id)
                is_valid = False
                num = ""
                cords = []
            elif not el.isnumeric() and not is_valid and num != "":
                is_valid = False
                num = ""
                cords = []
        if el.isnumeric() and is_valid and num != "":
            num_id += 1
            valid_points.append(int(num))
            for cord in cords:
                part_numbers_cords[cord] = (int(num), num_id)
    part_nums = set(valid_points)
    print(part_nums)
    # part 2
    print(part_numbers_cords)
    res = 0
    for i, row in enumerate(input_):
        for j, el in enumerate(row):
            if el == "*":
                cur_parts = set()
                for adj in adjacent_list:
                    part = part_numbers_cords.get((i + adj[0], j + adj[1]), None)
                    if part:
                        cur_parts.add(part)
                if len(cur_parts) == 2:
                    ratio = 1
                    for p in cur_parts:
                        ratio *= p[0]
                    res += ratio
    print(res)


solve()
