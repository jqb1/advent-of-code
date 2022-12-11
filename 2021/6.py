def read_input():
    with open("/Users/jkoziol/Downloads/input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


print(read_input()[0])


def day_change(lat, r):
    lats_to_add = []
    for day in range(r):
        for i in range(len(lat)):
            print(day)
            if lat[i] == 0:
                lat[i] = 6
                lats_to_add.append(8)
            else:
                lat[i] -= 1
        lat.extend(lats_to_add)
        lats_to_add.clear()
    return lat


# each lanternfish creates a new lanternfish once every 7 days
spawn_period = 7

laterns = list(map(int, read_input()[0].split(',')))
laterns_to_add = []
print(laterns)

# task1
# laterns = day_change(laterns, 80)

left = 256
lats_cnt = len(laterns)
day_ = 0
# doubles every 7 days
day = 252

print(len(laterns))
