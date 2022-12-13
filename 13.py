def read_input():
    with open("/Users/jkoziol/Downloads/input.txt") as f:
        lines = [eval(line.rstrip()) for line in f if not line == '\n']
    return lines


def compare_list_items(ll, lr):
    for i in range(len(ll)):
        try:
            lr[i]
        except IndexError:
            print(ll, lr, "Right side ran out of items")
            return False
        if type(ll[i]) is list and type(lr[i]) is list:
            result = compare_list_items(ll[i], lr[i])
            if result != 'Draw':
                return result
        elif type(ll[i]) is int and type(lr[i]) is list:
            result = compare_list_items([ll[i]], lr[i])
            if result != 'Draw':
                return result
        elif type(ll[i]) is list and type(lr[i]) is int:
            result = compare_list_items(ll[i], [lr[i]])
            if result != 'Draw':
                return result
        elif type(ll[i]) is int and type(lr[i]) is int:
            if ll[i] > lr[i]:
                print(ll[i], lr[i], "Right side is smaller")
                return False
            if ll[i] < lr[i]:
                return True
    return True if len(ll) < len(lr) else 'Draw'


indices = set()
packets = read_input()
packets_sorted = False

packets.extend([[[2]], [[6]]])

# bubble sort
while not packets_sorted:
    results = []
    for i in range(len(packets) - 1):
        l1 = packets[i][:]
        l2 = packets[i + 1][:]

        order = compare_list_items(l1, l2)
        # if res and res != 'Draw':
        if not order:
            packets[i] = l2[:]
            packets[i + 1] = l1[:]
            results.append(False)
        else:
            results.append(True)
            print((i // 2) + 1, "is ok")
            indices.add((i // 2) + 1)
    if all(results):
        packets_sorted = True

print(packets_sorted)
print(packets)
print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))

