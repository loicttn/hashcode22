from re import S

from typing import List

import sys


class Skill:
    def __init__(self, name: str, level: int) -> None:
        self.name: str = name
        self.level: int = level


class Developper:
    def __init__(self) -> None:
        self.skills: List[Skill] = []

        # day where the dev is hooked to a project
        self.calendar = []


class Project:
    def __init__(self, name: str, days: int, score: int, best: int, nb_skill: int) -> None:
        self.name = name
        self.days = days
        self.score = score
        self.best = best
        self.nb_skill = nb_skill
        self.skills: List[Skill] = []


def parse():
    with open(sys.argv[1], "r") as f:
        c = f.readlines()


if __name__ == '__main__':
    parse()
