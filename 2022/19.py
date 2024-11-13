import re
from collections import deque, namedtuple


def read_input():
    with open("./input.txt") as f:
        lines = [line.rstrip() for line in f]
    return lines


# find the best blueprint
# how many geodes it can open


def main():
    blueprints = {}
    for line in read_input()[:3]:
        (
            blueprint,
            ore_r_ore,
            clay_r_ore,
            obsidian_r_ore,
            obsidian_r_clay,
            geode_r_ore,
            geode_r_obsidian,
        ) = re.match(
            r"Blueprint (\d+): Each ore robot costs (\d) ore."
            r" Each clay robot costs (\d) ore. Each obsidian robot costs"
            r" (\d) ore and (\d+) clay. Each geode robot costs (\d)"
            r" ore and (\d+) obsidian.",
            line,
        ).groups()
        blueprints[int(blueprint)] = {
            "ore_robot_ore": int(ore_r_ore),
            "clay_robot_ore": int(clay_r_ore),
            "obsidian_robot_ore": int(obsidian_r_ore),
            "obsidian_robot_clay": int(obsidian_r_clay),
            "geode_robot_ore": int(geode_r_ore),
            "geode_robot_obsidian": int(geode_r_obsidian),
        }
    print(blueprints)

    quality_lvl = 1
    for k, blueprint in blueprints.items():
        geode = dfs_blueprint(blueprint)
        quality_lvl *= geode
    print(quality_lvl)


def dfs_blueprint(blueprint):
    time_limit = 32
    (
        req_ore_r_ore,
        req_clay_r_ore,
        req_obsidian_r_ore,
        req_obsidian_r_clay,
        req_geode_r_ore,
        req_geode_r_obsidian,
    ) = blueprint.values()

    # we have one ore-collecting robot
    # each robot can collect 1 of its resource per minute
    # 1 minute for the robot factory to construct any type of robot
    # factory consumes the necessary resources when construction begins
    Resources = namedtuple("Resources", ["ore", "clay", "obsidian", "geode"])
    Robots = namedtuple("Robots", ["ore", "clay", "obsidian", "geode"])
    q = deque(
        [
            (
                Resources(ore=0, clay=0, obsidian=0, geode=0),
                Robots(ore=1, clay=0, obsidian=0, geode=0),
                time_limit,
            )
        ]
    )
    max_geode = 0

    max_ore = max((req_ore_r_ore, req_clay_r_ore, req_obsidian_r_ore, req_geode_r_ore))
    min_ore = min((req_ore_r_ore, req_clay_r_ore, req_obsidian_r_ore, req_geode_r_ore))
    visited = set()
    while q:
        resources, robots, minutes = q.popleft()
        if minutes == 0:
            if resources.geode > max_geode:
                max_geode = resources.geode
                print(max_geode, minutes, resources, robots)
            continue
        if (resources, robots, minutes) in visited:
            continue
        visited.add((resources, robots, minutes))
        if resources.geode + robots.geode * (minutes - 1) < max_geode:
            continue
        print(robots, resources, minutes, max_geode)
        if resources.geode > max_geode:
            max_geode = resources.geode
            print(max_geode)
        # not adding any robot
        if (
            resources.ore < min_ore
            or resources.clay < req_obsidian_r_clay
            or resources.obsidian < req_geode_r_obsidian
        ):
            q.append(
                (
                    Resources(
                        ore=resources.ore + robots.ore,
                        clay=resources.clay + robots.clay,
                        obsidian=resources.obsidian + robots.obsidian,
                        geode=resources.geode + robots.geode,
                    ),
                    robots,
                    minutes - 1,
                )
            )

        # adding robots
        if resources.ore >= req_ore_r_ore and max_ore > robots.ore:
            q.append(
                (
                    Resources(
                        ore=resources.ore - req_ore_r_ore + robots.ore,
                        clay=resources.clay + robots.clay,
                        obsidian=resources.obsidian + robots.obsidian,
                        geode=resources.geode + robots.geode,
                    ),
                    Robots(
                        ore=robots.ore + 1,
                        clay=robots.clay,
                        obsidian=robots.obsidian,
                        geode=robots.geode,
                    ),
                    minutes - 1,
                )
            )
        # we don't need more clay robots than required clay per minute
        if resources.ore >= req_clay_r_ore and req_obsidian_r_clay > robots.clay:
            q.append(
                (
                    Resources(
                        ore=resources.ore - req_clay_r_ore + robots.ore,
                        clay=resources.clay + robots.clay,
                        obsidian=resources.obsidian + robots.obsidian,
                        geode=resources.geode + robots.geode,
                    ),
                    Robots(
                        ore=robots.ore,
                        clay=robots.clay + 1,
                        obsidian=robots.obsidian,
                        geode=robots.geode,
                    ),
                    minutes - 1,
                )
            )
        if (
            resources.ore >= req_obsidian_r_ore
            and resources.clay >= req_obsidian_r_clay
            and req_geode_r_obsidian > robots.obsidian
        ):
            q.append(
                (
                    Resources(
                        ore=resources.ore - req_obsidian_r_ore + robots.ore,
                        clay=resources.clay - req_obsidian_r_clay + robots.clay,
                        obsidian=resources.obsidian + robots.obsidian,
                        geode=resources.geode + robots.geode,
                    ),
                    Robots(
                        ore=robots.ore,
                        clay=robots.clay,
                        obsidian=robots.obsidian + 1,
                        geode=robots.geode,
                    ),
                    minutes - 1,
                )
            )

        if (
            resources.ore >= req_geode_r_ore
            and resources.obsidian >= req_geode_r_obsidian
        ):
            q.append(
                (
                    Resources(
                        ore=resources.ore - req_geode_r_ore + robots.ore,
                        clay=resources.clay + robots.clay,
                        obsidian=resources.obsidian
                        - req_geode_r_obsidian
                        + robots.obsidian,
                        geode=resources.geode + robots.geode,
                    ),
                    Robots(
                        ore=robots.ore,
                        clay=robots.clay,
                        obsidian=robots.obsidian,
                        geode=robots.geode + 1,
                    ),
                    minutes - 1,
                )
            )

    return max_geode


if __name__ == "__main__":
    main()
