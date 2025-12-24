from itertools import combinations
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

with open("input10.txt", "r") as f:
    lines = f.read().splitlines()
    p1 = 0
    p2 = 0
    for line in lines:
        final = list(map(lambda x : 1 if x == "#" else 0, list(line.split("] ")[0][1:])))
        buttons = list(map(lambda x : tuple(map(int, x[1:-1].split(","))), line.split("] ")[1].split(" {")[0].split()))
        joltages = list(map(int, line.split(" {")[1][:-1].split(",")))
        
        for n in range(len(buttons) + 1):
            for comb in combinations(buttons, n):
                if [sum(i in p for p in comb)%2 for i in range(len(final))] == final:
                    p1 += len(comb)
                    break
            else:
                continue
            break

        A = np.array([[1 if i in x else 0 for x in buttons] for i in range(len(final))])
        j = np.array(joltages)
        n_vars = len(buttons)
        c = np.ones(n_vars)
        constraints = LinearConstraint(A, j, j)
        integrality = np.ones(n_vars)
        
        result = milp(c=c, constraints=constraints, integrality=integrality)
        p2 += int(np.sum(result.x))
    print("Part 1:", p1)
    print("Part 2:", p2)