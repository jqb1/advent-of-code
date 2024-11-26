from collections import Counter

from utils import ints, vadd


def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip().split(", ") for line in f]
    return lines


def puzzle():
    inp = read_input()
    particles = []
    for i, line in enumerate(inp):
        p, v, a = map(lambda x: ints(x), line)
        particles.append((tuple(map(int, p)), tuple(map(int, v)), tuple(map(int, a))))

    for tick in range(50):
        new_particles = []
        pc = Counter([p for p, v, a in particles])
        for p, v, a in particles:
            if pc[p] > 1:
                continue
            v = vadd(v, a)
            p = vadd(p, v)
            new_particles.append((p, v, a))
        particles = new_particles
    print(len(particles))


puzzle()
