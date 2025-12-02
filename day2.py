from itertools import batched

with open("input2.txt", "r") as f:
    ranges = [list(map(int, r.split("-"))) for r in f.read().split(",")]
    p1 = 0
    p2 = 0
    for r in ranges:
        for id in range(r[0], r[1] + 1):
            s = str(id)
            id_len = len(str(id))
            invalid = set()
            for d in range(1, id_len):
                if id_len % d == 0:
                    chunks = list(batched(list(str(id)), n=d))
                    if chunks.count(chunks[0]) == len(chunks):
                        invalid.add(id)
                        if d == id_len/2:
                            p1 += id
            p2 += sum(invalid)
    print("Part 1:", p1)
    print("Part 2:", p2)