#Uses python3

import sys

def toposort(adj):
    order = []

    def visit(v):


        visited[v] = 1

        for i in adj[v]:
            if not visited[i]:
                visit(i)

        order.insert(0, v)

    visited = [0] * len(adj)

    for i in range(len(adj)):

        if not visited[i]:
            visit(i)

    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')
