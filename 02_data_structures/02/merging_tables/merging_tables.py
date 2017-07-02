# python3

import sys

sys.setrecursionlimit(10**7)

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))

ans = max(lines)

def getParent(table):

    path = []

    while table != parent[table]:
        path.append(table)
        table =  parent[table]

    for i in range(len(path)):
        parent[path[i]] = table

    return table

    # if parent[table] != table:
    #     parent[table] =  getParent(parent[table])
    #
    # return parent[table]

def merge(destination, source):

    #print('marge', destination, source)
    #print(parent, lines, rank)

    realDestination, realSource = getParent(destination), getParent(source)

    #print('real', realDestination, realSource)

    if realDestination != realSource:

        rows = lines[realSource] + lines[realDestination]

        if rank[realDestination] > rank[realSource]:

            parent[realDestination] = realSource
            lines[realSource] = rows

            lines[realDestination] = 0

        else:
            parent[realSource] = realDestination
            lines[realDestination] = rows

            lines[realSource] = 0

            if rank[realDestination] == rank[realSource]:
                rank[realSource] += 1


        # merge two components
        # use union by rank heuristic
        # update ans with the new maximum table size

        #print(lines[realDestination])
        #print(ans)

    return lines[realDestination]

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())

    #(destination, source)
    #print(destination, source)
    ans = max(ans, merge(destination - 1, source - 1))
    print(ans)
