from math import prod
import re

with open("input6.txt", "r") as f:
    lines = f.read().splitlines()
    regex = r'\s+'
    ops = re.split(regex, lines.pop(-1).strip())
    lines2 = list(map(lambda l : list(l + ' '), lines))
    lines = list(map(lambda l : list(map(int, re.split(r'\s+', l.strip()))), lines))
    
    p1 = 0
    for op, nums in zip(ops, zip(*lines)):
        if op == '*':
            p1 += prod(nums)
        elif op == '+':
            p1 += sum(nums)
    print("Part 1:", p1)

    p2 = 0
    i = 0
    l = []
    for p in zip(*lines2):
        if all(map(lambda x : x == ' ', p)):
            if ops[i] == '*':
                p2 += prod(l)
            elif ops[i] == '+':
                p2 += sum(l)
            i += 1
            l.clear()
            continue
        l.append(int("".join(p)))
    print("Part 2:", p2)
        