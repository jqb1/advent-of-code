# test code
# while a != 0:
#     a = a // 2 ** 3
#     print(a % 8)
# we want 0,3,5,4,3,0  6 prints

# real code
def run(a):
    new_n = []
    while a != 0:
        b = a % 8  # 2,4
        b = b ^ 5  # 1, 5
        c = a // 2**b  # 7,5
        b = b ^ c  # 4, 3
        b = b ^ 6  # 1, 6
        a = a // 2**3  # 0, 3
        new_n.append(b % 8)
    return new_n


program = [2, 4, 1, 5, 7, 5, 4, 3, 1, 6, 0, 3, 5, 5, 3, 0]
cur_a = 0
for n in range(len(program)):
    pos_val = cur_a * 2**3
    for i in range(10**5):
        pos_val += 1
        out = run(pos_val)
        if out and out == program[-n - 1 :]:
            print("found", i)
            cur_a = pos_val
            print(out, pos_val, bin(cur_a))
            break
print(cur_a)
print(run(cur_a))
