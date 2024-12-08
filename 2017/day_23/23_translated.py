"""23 asm roughly translated to py3"""


def translated_run():
    d, e, f, g, h = 0, 0, 0, 0, 0
    b = 109300
    c = 126300
    g = None
    # b=109300, c = 126300, f=1
    while True:
        f, d, e = 1, 2, 2
        while d != b:
            while e != b:
                g = d
                g = g * e
                g -= b
                if g == b:
                    f = 0
                e += 1
            d += 1
        if f == 0:
            h += 1
        if b == c:
            return h
        b += 17
