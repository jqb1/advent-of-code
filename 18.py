import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt


def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


def all_cubes_cords(cube_array):
    cords = set()
    for x, y, z in zip(*np.nonzero(cube_array)):
        cords.add((x, y, z))

    return cords


def main():
    cubes = {tuple(map(int, line.split(','))) for line in read_input()}

    min_z, max_z = min(cubes, key=lambda x: x[2])[2], max(cubes, key=lambda x: x[2])[2]
    min_y, max_y = min(cubes, key=lambda x: x[1])[1], max(cubes, key=lambda x: x[1])[1]
    min_x, max_x = min(cubes, key=lambda x: x[0])[0], max(cubes, key=lambda x: x[0])[0]

    droplet = np.zeros((max_x + 1, max_y + 1, max_z + 1), dtype=int)

    for cube in cubes:
        x, y, z = cube
        droplet[x][y][z] = 1
    # part1
    print(all_cubes_cords(droplet))
    c = 0
    all_cubes = all_cubes_cords(droplet)
    for cube in all_cubes:
        c += count_external_sides(cube, all_cubes)
    print(c)

    # part 2
    filled_droplet = scipy.ndimage.binary_fill_holes(droplet).astype(int)
    all_cubes_filled = all_cubes_cords(filled_droplet)
    c_2 = 0
    for cube in all_cubes_filled:
        c_2 += count_external_sides(cube, all_cubes_filled)

    print(c_2)

    # display the shape for fun
    ax = plt.axes(projection='3d')
    ax.set_facecolor("#6666ff")
    ax.voxels(filled_droplet, facecolor="#E02050", edgecolor='white')
    ax.axis("off")
    plt.show()

def count_external_sides(cube, all_cords):
    x, y, z = cube
    left = (x - 1, y, z)
    right = (x + 1, y, z)
    up = (x, y + 1, z)
    down = (x, y - 1, z)
    front = (x, y, z + 1)
    back = (x, y, z - 1)

    cntr = 0
    for dir in (left, right, up, down, front, back):
        cntr += 1 if dir not in all_cords else 0

    return cntr





if __name__ == '__main__':
    main()