#!/usr/bin/env python3

from re import S

from typing import List, Tuple

import sys


class Skill:
    def __init__(self, name: str, level: int) -> None:
        self.name: str = name
        self.level: int = level

    def increment_level(self):
        self.level += 1

    def __str__(self):
        return f'<Skill {self.name} lvl.{self.level}>'


class Developper:
    def __init__(self, name: str, nb_skills: int) -> None:
        self.name = name
        self.nb_skills = nb_skills
        self.skills: List[Skill] = []

        # day where the dev is hooked to a project
        self.calendar = []

    def __str__(self) -> str:
        s = " - ".join(map(lambda x: x.__str__(), self.skills))
        return f"<Dev name: {self.name} nb_skills: {self.nb_skills}\n SKILLS: {s}>"

    def assign_skill(self, skill: Skill) -> None:
        self.skills.append(skill)


class Project:
    def __init__(self, name: str, days: int, score: int, best: int, nb_skill: int) -> None:
        self.name = name
        self.days = days
        self.score = score
        self.best = best
        self.nb_skill = nb_skill
        self.required_skills: List[Skill] = []

    def assign_required_skill(self, skill: Skill) -> None:
        self.required_skills.append(skill)

    def __str__(self):
        s = " - ".join(map(lambda x: x.__str__(), self.required_skills))
        return f'<Project {self.name} days {self.days} score {self.score} best {self.best} nb_skills {self.nb_skill} {s}>'


def parseProjectLine(line: str) -> Project:
    spl = line.split(" ")
    return Project(spl[0], int(spl[1]), int(spl[2]), int(spl[3]), int(spl[4]))


def parseSkillLine(line: str) -> Skill:
    spl = line.split(" ")
    return Skill(spl[0], int(spl[1]))


def parseDevelopperLine(line: str) -> Developper:
    spl = line.split(" ")
    return Developper(spl[0], int(spl[1]))


def nnl(s: str) -> str:
    return s[:len(s)-1]


def parse():
    with open(sys.argv[1], "r") as f:
        c = f.readlines()
        head = list(map(int, c[0].split(" ")))
        contributors_nb = head[0]
        projects_nb = head[1]
        x = 1
        devs = []
        projects = []
        for _ in range(contributors_nb):
            dev = parseDevelopperLine(nnl(c[x]))
            x += 1
            for _ in range(dev.nb_skills):
                s = parseSkillLine(nnl(c[x]))
                dev.assign_skill(s)
                x += 1
            devs.append(dev)
        for _ in range(projects_nb):
            project = parseProjectLine(nnl(c[x]))
            x += 1
            for _ in range(project.nb_skill):
                s = parseSkillLine(nnl(c[x]))
                project.assign_required_skill(s)
                x += 1
            projects.append(project)
    return devs, projects


if __name__ == '__main__':
    devs, projects = parse()
    print("DEVS")
    for d in devs:
        print(d)
    print("PROJECTS")
    for p in projects:
        print(p)
