from copy import deepcopy

with open("input11.txt", "r") as f:
    outputs = {x.split(": ")[0]: x.split(": ")[1].split() for x in f.read().splitlines()}
    outputs["out"] = []

    topOrder = []
    outputsCopy = deepcopy(outputs)
    while True:
        flag = True

        for n in outputsCopy:
            if len(outputsCopy[n]) == 0:
                outputsCopy.pop(n)
                topOrder.append(n)
                for v in outputsCopy:
                    if n in outputsCopy[v]:
                        outputsCopy[v].remove(n)
                flag = False
                break

        if flag:
            break;
    
    paths = {"out": 1}
    for n in topOrder[1:]:
        paths[n] = sum(paths[x] for x in outputs[n])
        if n == "you":
            break;
    print("Part 1:", paths["you"])

    ## (none, fft, dac, both)
    paths = {"out": (1, 0, 0, 0)}
    for n in topOrder[1:]:        
        s = list(map(sum, zip(*(paths[x] for x in outputs[n]))))
        if n == "fft":
            if s[2] > 0:
                s[3] = s[2]
            else:
                s[1] = s[0]
        elif n == "dac":
            if s[1] > 0:
                s[3] = s[1]
            else:
                s[2] = s[0]
            
            
        paths[n] = tuple(s)
        if n == "svr":
            break
    print("Part 2:", paths["svr"][3])