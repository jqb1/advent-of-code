def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip().split(":") for line in f]
    return lines


def solve():
    input_ = read_input()
    powers = []
    for game in input_:
        game_id = game[0][5:]
        cube_plays = game[1].split(";")
        powers.append(check_possible_game(cube_plays))
    return sum(powers)


def check_possible_game(cube_plays):
    cube_num = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for play in cube_plays:
        for color in play.split(","):
            _, num, color = color.split(" ")
            num = int(num)
            if num > cube_num[color]:
                cube_num[color] = num
    return cube_num["red"] * cube_num["green"] * cube_num["blue"]


solution = solve()
print(solution)
