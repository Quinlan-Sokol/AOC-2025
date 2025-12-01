with open('input1.txt', 'r') as file:
    lines = file.read().splitlines()
    pos = 50
    p1 = 0
    p2 = 0
    for line in lines:
        amount = int(line[1:])
        step = (1 if line[0] == "R" else -1)
        start = pos
        pos = (pos + step * amount) % 100
        if pos == 0:
            p1 += 1
        k_first = (-start * pow(step, -1, 100)) % 100
        if k_first == 0:
            k_first = 100
        if k_first <= amount:
            p2 += 1 + (amount - k_first) // 100
    print("Part 1:", p1);
    print("Part 2:", p2);