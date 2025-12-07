with open("input7.txt", "r") as f:
    grid = [list(x) for x in f.read().splitlines()]
    
    start_pos = (0,0)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start_pos = (j, i)
    
    p1 = 0
    seen = dict()
    def search(p):
        global p1, seen
        if p[1] >= len(grid):
            seen[p] = 1 
            return
        
        if p in seen:
            return

        if grid[p[1]][p[0]] == '^':
            p1 += 1
            search((p[0] + 1, p[1] + 1))
            search((p[0] - 1, p[1] + 1))
            seen[p] = seen[(p[0] + 1, p[1] + 1)] + seen[(p[0] - 1, p[1] + 1)]
        else:
            search((p[0], p[1] + 1))
            seen[p] = seen[(p[0], p[1] + 1)]
        

       
    search(start_pos)
    print("Part 1:", p1)
    print("Part 2:", seen[start_pos])
