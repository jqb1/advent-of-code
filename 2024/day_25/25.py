from utils import read_input


def solve():
    schemas = read_input().split("\n\n")
    locks, keys = [], []
    for schema in schemas:
        schema = schema.split("\n")
        if schema[0] == "#####" and schema[-1] == ".....":
            keys.append(
                {
                    (r, c)
                    for r, row in enumerate(schema)
                    for c, pin in enumerate(row)
                    if pin == "#"
                }
            )
        else:
            locks.append(
                {
                    (r, c)
                    for r, row in enumerate(schema)
                    for c, pin in enumerate(row)
                    if pin == "#"
                }
            )

    ans = 0
    for key in keys:
        for lock in locks:
            if not key & lock:
                ans += 1
    print(ans)


if __name__ == "__main__":
    solve()
