from collections import deque


def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


def main():
    # faster lookup
    closing_chars = {")", "]", "}", ">"}
    opening_chars = {"(", "[", "{", "<"}

    chunk_open_to_close = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }
    points_sum = solve_part1(opening_chars, closing_chars, chunk_open_to_close)
    print("part1:", points_sum)
    solve_part2(opening_chars, closing_chars, chunk_open_to_close)


def solve_part1(opening_chars, closing_chars, chunk_open_to_close):
    """checking the corrupted lines"""
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    points_sum = 0
    for line in read_input():
        opened = deque([])
        for token in line:
            if token in opening_chars:
                opened.append(token)
            elif token in closing_chars:
                last_opened = opened.pop()
                if token != chunk_open_to_close[last_opened]:
                    points_sum += points[token]
                    break
    return points_sum


def solve_part2(opening_chars, closing_chars, chunk_open_to_close):
    """finishing unfinised lines"""
    points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    scores = []
    for line in read_input():
        opened = deque([])
        corrupted = False
        for token in line:
            if token in opening_chars:
                opened.append(token)
            elif token in closing_chars:
                last_opened = opened.pop()
                if token != chunk_open_to_close[last_opened]:
                    corrupted = True
                    break
        score = 0
        if not corrupted and opened:
            while opened:
                last_opened = opened.pop()
                closing_token = chunk_open_to_close[last_opened]
                score = score * 5 + points[closing_token]
            scores.append(score)
    print(sorted(scores))
    print("part2:", sorted(scores)[len(scores) // 2])


if __name__ == "__main__":
    main()
