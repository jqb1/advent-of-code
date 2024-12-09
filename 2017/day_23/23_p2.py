#  of 23_translated asm translation

# asm program counts non-prime numbers between b and c step 17
# asm input https://adventofcode.com/2017/day/23/input


def solve():
    b = 109300
    c = 126300
    h = 0
    while b <= c + 1:
        if not is_prime(b):
            h += 1
        b += 17
    print(h)


def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


solve()
