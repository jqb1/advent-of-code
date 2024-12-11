import os
import re
from typing import Iterable, List

import requests

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

# direction delta in 2x2 grid
DIRECTION = {
    "l": (0, -1),
    "r": (0, 1),
    "u": (-1, 0),
    "d": (1, 0),
}

TURN = {
    # d = current direction
    # (d, turn): (result)
    ("r", "r"): "d",
    ("r", "l"): "u",
    ("l", "l"): "d",
    ("l", "r"): "u",
    ("u", "r"): "r",
    ("u", "l"): "l",
    ("d", "l"): "r",
    ("d", "r"): "l",
}


def ints(line: str) -> tuple:
    return tuple(re.findall(r"(-?\d+)", line))


def digits(line: str) -> tuple:
    return tuple(re.findall(r"(\d)", line))


def vadd(v1: Iterable[int], v2: Iterable[int]) -> tuple:
    """add two vectors"""
    return tuple([x1 + x2 for x1, x2 in zip(v1, v2)])


def submit(answer: int | str, part=1):
    _init_env()
    day, year, session, user = (
        os.environ["day"],
        os.environ["year"],
        os.environ["session"],
        os.environ["user"],
    )
    ans = (
        str(
            input(
                f"==> Submitting day \033[38;5;15m{day}\033[0m part \033[38;5;15m{part}\033[0m, answer \033[38;5;15m{answer}?\033[0m y/N/2"
            )
        )
        .lower()
        .strip()
    )
    if ans == "n":
        print("Not submitting")
        return
    elif ans == "2":
        ans = str(input(f"Submitting part 2, answer {answer}? y/N")).lower().strip()
        if ans != "y":
            print("Not submitting")
            return
        part = 2
    if ans == "y":
        print(f"---Submitting part {part} answer {answer}---")
        resp = requests.post(
            f"https://adventofcode.com/{year}/day/{day}/answer",
            headers={
                "Cookie": f"session={session}",
                # https://www.reddit.com/r/adventofcode/comments/z9dhtd/please_include_your_contact_info_in_the_useragent/?rdt=53988
                "User-Agent": f"https://github.com/jqb1/advent-of-code by {user}",
            },
            data={"answer": answer, "level": part},
        )

        for line in str(resp.content).split("\\n"):
            if "answer" in line or "level" in line:
                print(line)


def read_input(test=False) -> str:
    _init_env()
    day, year = (
        os.environ["day"],
        os.environ["year"],
    )
    filename = (
        f"{DIR_PATH}/{year}/day_{day}/input.txt"
        if not test
        else f"{DIR_PATH}/{year}/day_{day}/input_t.txt"
    )
    if not os.path.isfile(filename) and not test:
        _download_input()
    with open(filename) as f:
        input_ = f.read()
    return input_


def _download_input():
    _init_env()
    day, year, session, user = (
        os.environ["day"],
        os.environ["year"],
        os.environ["session"],
        os.environ["user"],
    )
    resp = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input",
        headers={
            "Cookie": f"session={session}",
            # https://www.reddit.com/r/adventofcode/comments/z9dhtd/please_include_your_contact_info_in_the_useragent/?rdt=53988
            "User-Agent": f"https://github.com/jqb1/advent-of-code by {user}",
        },
    )
    with open(f"{DIR_PATH}/{year}/day_{day}/input.txt", mode="w") as f:
        f.write(resp.text)


def _init_env():
    session = os.environ.get("session")
    if session:
        return
    with open(f"{DIR_PATH}/session.ini") as f:
        lines = [line.rstrip().split(" = ") for line in f.readlines()]
        for key, value in lines:
            if key not in {"day", "session", "year", "user"}:
                print(f"Unknown key {key} in session.ini")
                continue
            os.environ[key] = value
