def read_input():
    with open("/Users/jkoziol/Downloads/input.txt") as f:
        moves = [line.rstrip() for line in f]
    return moves


head_moves = read_input()
print(head_moves)

pos_change = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0)
}


def check_tail(tail_pos, head_pos):
    dr = abs(tail_pos[0] - head_pos[0])
    dc = abs(tail_pos[1] - head_pos[1])
    return dr >= 2 or dc >= 2


def move_tail(tail_pos_, head_pos_):
    dr, dc = 0, 0
    # same row
    if tail_pos_[0] == head_pos_[0]:
        if tail_pos_[1] < head_pos_[1]:
            dc = 1
        elif tail_pos_[1] > head_pos_[1]:
            dc = -1
    # same col
    elif tail_pos_[1] == head_pos_[1]:
        if tail_pos_[0] < head_pos_[0]:
            dr = 1
        if tail_pos_[0] > head_pos_[0]:
            dr = -1
    # different
    else:
        if tail_pos_[0] < head_pos_[0] and tail_pos_[1] < head_pos_[1]:
            dr = 1
            dc = 1
        elif tail_pos_[0] > head_pos_[0] and tail_pos_[1] < head_pos_[1]:
            dr = -1
            dc = 1
        elif tail_pos_[0] < head_pos_[0] and tail_pos_[1] > head_pos_[1]:
            dr = 1
            dc = -1
        else:
            dr = -1
            dc = -1
    return dr, dc


pos_head = [1000, 1000]
pos_tail = [1000, 1000]
start_pos = (1000, 1000)
tail_moves = [(1000, 1000)]
pos_prev_head = pos_head

rope_pos = [[1000, 1000] for _ in range(10)]
for move in head_moves:
    direc_, steps = move.split()
    steps = int(steps)
    print(direc_, steps)
    for step in range(steps):
        row_c, col_c = pos_change[direc_]
        pos_prev_head = rope_pos[0][:]
        # head position change
        rope_pos[0][0] += row_c
        rope_pos[0][1] += col_c

        for i in range(1, len(rope_pos)):
            if check_tail(rope_pos[i], rope_pos[i - 1]):
                dr, dc = move_tail(rope_pos[i], rope_pos[i-1])
                rope_pos[i][0] += dr
                rope_pos[i][1] += dc
                if i == 9:
                    tail_moves.append(tuple(rope_pos[i]))

print(set(tail_moves))
print(len(set(tail_moves)))
