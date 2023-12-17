from collections import deque


def read_input():
    with open("./input.txt") as f:
        lines = [[l for l in line.rstrip()] for line in f]
    return lines


DIRECTION = {
    'l': (0, -1),
    'r': (0, 1),
    'u': (-1, 0),
    'd': (1, 0),
}

MIRROR = {
    "\\": {"u": "l", "r": "d", "l": "u", "d": "r"},
    "/": {"u": "r", "r": "u", "l": "d", "d": "l"},
}

SPLITTER = {
    "|": {"u": ["u"], "d": ["d"], "l": ["u", "d"], "r": ["u", "d"]},
    "-": {"u": ["l", "r"], "d": ["l", "r"], "l": ["l"], "r": ["r"]}
}


def solve():
    map_ = read_input()
    print(map_)
    max_r, max_c = len(map_)-1, len(map_[0])-1
    # part 1
    # possible_start = [(0, 0, "r")]
    #part 2
    possible_start = [*[(r, -1, "r") for r in range(max_r+1)],
                      *[(-1, c, "d") for c in range(max_c+1)],
                      *[(max_r+1, c, "u") for c in range(max_c+1)],
                      *[(r, max_c+1, "l") for r in range(max_r+1)],
    ]

    max_result = 0
    for start in possible_start:
        q = deque([start])
        seen = set()
        visited = set()
        while q:
            beam = q.popleft()
            if beam in seen:
                continue
            seen.add(beam)
            br, bc, b_dir = beam
            dr, dc = DIRECTION[b_dir]
            br += dr
            bc += dc
            if bc > max_c or bc < 0 or br > max_r or br < 0:
                continue
            visited.add((br, bc))
            el = map_[br][bc]

            beam = (br, bc, b_dir)
            if el in MIRROR:
                beam = (br, bc, MIRROR[el][b_dir])
            elif el in SPLITTER:
                new_directions = SPLITTER[el][b_dir]
                if len(new_directions) == 2:
                    beam = (br, bc, new_directions[0])
                    q.append((br, bc, new_directions[1]))
            q.append(beam)
        max_result = max(max_result, len(visited))
        print(len(visited))
    print(max_result)
solve()
