from copy import deepcopy

with open("input5.txt", "r") as f:
    part1, part2 = f.read().split("\n\n")
    ranges = [(int(x.split("-")[0]), int(x.split("-")[1])) for x in part1.splitlines()]
    ids = list(map(int, part2.splitlines()));
    
    p1 = 0
    for id in ids:
        for r in ranges:
            if r[0] <= id <= r[1]:
                p1 += 1
                break
    print("Part 1:", p1)

    while True:
        for i in range(len(ranges)):
            for j in range(i+1, len(ranges)):
                r1 = ranges[i]
                r2 = ranges[j]
                if r1[0] <= r2[0] <= r1[1] <= r2[1]:
                    ranges[i] = (r1[0], r2[1])
                    ranges.pop(j)
                    break
                if r2[0] <= r1[0] <= r2[1] <= r1[1]:
                    ranges[i] = (r2[0], r1[1])
                    ranges.pop(j)
                    break
                if r1[0] <= r2[0] <= r2[1] <= r1[1]:
                    ranges.pop(j)
                    break
                if r2[0] <= r1[0] <= r1[1] <= r2[1]:
                    ranges.pop(i)
                    break
            else:
                continue
            break
        else:
            break
    print("Part 2:", sum(map(lambda r : r[1] - r[0] + 1, ranges)))
