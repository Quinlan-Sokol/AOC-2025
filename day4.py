from copy import deepcopy

with open("input4.txt", "r") as f:
    grid = [list(x) for x in f.read().splitlines()]
    p1 = 0
    p2 = 0
    num_removed = 1
    i = 0
    while num_removed > 0:
        num_removed = 0
        i += 1
        new_grid = deepcopy(grid)
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == '@':
                    c = 0
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if (dx != 0 or dy != 0) and 0 <= y + dy < len(grid) and 0 <= x + dx < len(grid[y]):
                                if grid[y + dy][x + dx] == '@':
                                    c += 1
                    if c < 4:
                        p2 += 1
                        new_grid[y][x] = '.'
                        num_removed += 1
                        if i == 1:
                            p1 += 1
        grid = new_grid
    print("Part 1:", p1)
    print("Part 2:", p2)