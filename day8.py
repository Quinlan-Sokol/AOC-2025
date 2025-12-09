from itertools import chain
from math import prod


def connect(connections, box, s):
    s.add(box)
    for c in connections:
        if c[0] == box:
            connections.remove(c)
            connect(connections, c[1], s)
        if c[1] == box:
            connections.remove(c)
            connect(connections, c[0], s)

def hasFullNetwork(networks, num):
    for n in networks:
        if len(set(chain(*n))) == num:
            return True
    return False


with open("input8.txt", "r") as f:
    coords = [tuple(map(int, l.split(','))) for l in f.read().splitlines()]
    dists = []

    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            dists.append((((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2 + (coords[i][2] - coords[j][2])**2)**.5, (coords[i], coords[j])))
    
    dists.sort(key=lambda x : x[0])
    connections = list(map(lambda x : x[1], dists))
    networks = []
    last = None
    count = 0
    while not hasFullNetwork(networks, len(coords)):
        c = connections.pop(0)
        l = []
        count += 1
        for i in range(len(networks)):
            if c[0] in map(lambda x : x[0], networks[i]) or c[1] in map(lambda x : x[0], networks[i]) or \
               c[0] in map(lambda x : x[1], networks[i]) or c[1] in map(lambda x : x[1], networks[i]):
                l.append(i)
                networks[i].add(c)
                last = c
        if len(l) == 0:
            s = set([c])
            networks.append(s)
        elif len(l) == 2:
            networks[l[0]].update(networks[l[1]])
            networks.pop(l[1])
        if count == 1000:
            print("Part 1:", prod(sorted(map(lambda n : len(set(chain(*n))), networks), reverse=True)[:3]))
    print("Part 2:", last[0][0] * last[1][0])

