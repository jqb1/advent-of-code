import heapq


def read_input():
    with open("./input.txt") as f:
        lines = [[int(el) for el in line.rstrip()] for line in f]
    return lines


DIRECTION = {
    'l': (0, -1),
    'r': (0, 1),
    'u': (-1, 0),
    'd': (1, 0),
}

POSSIBLE_TURNS = {
    'l': ['u', 'd'],
    'r': ['u', 'd'],
    'u': ['l', 'r'],
    'd': ['l', 'r'],
    None: ['r', 'd'],  # starting point
}


def solve():
    heat_map = read_input()
    print(heat_map)

    # min heap queue: (heat, (row, col), direction, straight_c)
    min_q = [(0, (0, 0), None, 0)]
    # unvisited = {(row, col): float("inf") for col in range(len(heat_map[0])) for row in range(len(heat_map))}
    # visited, best results for each point
    lowest_loss = {}

    max_row = len(heat_map) - 1
    max_col = len(heat_map[0]) - 1
    end_point = (max_row, max_col)

    while min_q:
        heat, node, dir_, straight_c = heapq.heappop(min_q)
        row, col = node
        if node == end_point:
            # print_map(max_row + 1, max_col + 1, heat_map, path)
            print("result:", heat)
            break
        if (node, dir_, straight_c) in lowest_loss:
            continue
        lowest_loss[(node, dir_, straight_c)] = heat
        if straight_c < 4 and dir_:
            turns = [dir_]
        elif 4 <= straight_c < 10:
            turns = POSSIBLE_TURNS[dir_] + [dir_]
        else:
            turns = POSSIBLE_TURNS[dir_]

        for turn in turns:
            dr, dc = DIRECTION[turn]
            neighbor_p = (row + dr, col + dc)
            # if out of bounds
            if neighbor_p[0] > max_row or neighbor_p[0] < 0 or neighbor_p[1] > max_col or neighbor_p[1] < 0:
                continue
            # if (cost := heat + heat_map[neighbor_p[0]][neighbor_p[1]]) < unvisited[neighbor_p]:
            cost = heat + heat_map[neighbor_p[0]][neighbor_p[1]]
            if turn == dir_:
                # unvisited[neighbor_p] = cost
                heapq.heappush(min_q, (cost, neighbor_p, turn, straight_c + 1))
            elif turn != dir_:
                # unvisited[neighbor_p] = cost
                heapq.heappush(min_q, (cost, neighbor_p, turn, 1))


def print_map(row_len, col_len, heat_map, path):
    s = 0
    for r in range(row_len):
        row = ""
        for col in range(col_len):
            if (r, col) in path:
                s += heat_map[r][col]
            row += " x" if (r, col) in path else f" {heat_map[r][col]}"
        print(row)


solve()
