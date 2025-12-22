with open("input12.txt", "r") as f:
    p1 = 0
    for line in f.read().splitlines():
        if "x" in line:
            w = int(line.split(": ")[0].split("x")[0])
            h = int(line.split(": ")[0].split("x")[1])
            presentArea = sum(map(int, line.split(": ")[1].split()))
            p1 += presentArea * 8 < w * h
    print(p1)