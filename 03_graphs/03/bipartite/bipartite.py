#Uses python3

import sys
from collections import deque

def bipartite(adj):

    n = len(adj)

    color = [None] * n

    q = deque([0])

    color[0] = 1

    while len(q):

        u = q.pop()

        for v in adj[u]:

            if color[v] == None:
                q.appendleft(v)
                if color[u] == 1:
                    color[v] = 2
                else:
                    color[v] = 1
            else:
                if color[u] == color[v]:
                    return 0

    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
