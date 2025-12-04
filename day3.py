from functools import cache

with open("input3.txt", "r") as f:
    banks = [list(map(int, b)) for b in  f.read().splitlines()]
    p1 = 0
    p2 = 0
    for bank in banks:
        @cache
        def findBest(p, n):
            if p == -1 or n == 0:
                return 0
            nopick = findBest(p - 1, n)
            pick = findBest(p - 1, n - 1) * 10 + bank[p]
            return max(nopick, pick)

        p1 += findBest(len(bank) - 1, 2)
        p2 += findBest(len(bank) - 1, 12)
    print("Part 1:", p1)
    print("Part 2:", p2)