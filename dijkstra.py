import math

def dijkstraRun(nodedic):
    #print(nodedic)
    start = 'S'
    end = 'E'
    checknodes = {keys:(math.inf, '') for keys in nodedic if keys != start and keys != end}
    #print('tick')
    prioritycue = ''
    for item in checknodes:
        prioritycue += item
    prioritycue = 'S'+prioritycue+'E'
    endlist = ''
    checknodes[start] = (0,'')
    checknodes[end] = (math.inf,'')
    # print(checknodes)
    #print('tick')
    while not prioritycue[0] == end:
        #print(prioritycue)
        check = prioritycue[0]
        prioritycue = prioritycue[1:] 
        for connectednode in nodedic[check]['connections']:
            if  connectednode == 'S':
                continue
                # print(nodedic[check]['connections'][connectednode][1]+checknodes[check][0], checknodes[connectednode])
            elif nodedic[check]['connections'][connectednode][1]+checknodes[check][0] < checknodes[connectednode][0]:
                checknodes[connectednode] = (nodedic[check]['connections'][connectednode][1]+checknodes[check][0], check)
                prioritycue = prioritycue[:prioritycue.find(connectednode)] + prioritycue[prioritycue.find(connectednode)+1:]
                for pos in range(len(prioritycue)):
                #print(pos, prioritycue[pos])
                #print('in priority cue', prioritycue)
                    if checknodes[prioritycue[pos]][0] > checknodes[connectednode][0]:
                        #print('tick')
                        prioritycue = prioritycue[:pos] + connectednode + prioritycue[pos:]
                        break
        
        #print(prioritycue)
        #print(checknodes)
        #print([(key, checknodes[key]) for key in prioritycue])
        endlist += check
    outlist = endlist[-1]
    check = outlist
    while not check == 'S':
        #print(checknodes[check][1])
        outlist = checknodes[check][1] + outlist

        check = outlist[0]
        #print(outlist, check)
    outlist+="E"
    return outlist
        
def printcoords(dirlist,nodedic):
    outlist = []
    for item in range(len(dirlist)):
        outlist.append(nodedic[dirlist[item]]['coordinate'])
        if not item == len(dirlist)-1:
            nextnode = nodedic[dirlist[item+1]]['coordinate']
            current = outlist[-1]
            if nextnode[0] == current[0]:
                if abs(current[1]-nextnode[1]) > 1:
                    if current[1] > nextnode[1]:
                        turn = -1
                    else:
                        turn = 1
                    for step in range(min(current[1],nextnode[1]), max(current[1],nextnode[1]), turn):
                        #print(current[0])
                        if step == current[1]:
                            continue
                        outlist.append((current[0],step)) 
            elif nextnode[1] == current[1]:
                if abs(current[0]-nextnode[0]) > 1:
                    if current[0] > nextnode[0]:
                        turn = -1
                    else:
                        turn = 1
                    for step in range(min(current[0],nextnode[0]), max(current[0],nextnode[0]), turn):
                        if step == current[0]:
                            continue
                        outlist.append((step,current[1])) 
    return outlist
        
