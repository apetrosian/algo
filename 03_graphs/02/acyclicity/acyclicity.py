#Uses python3

import sys

def acyclic(adj):

    def visit(v):

        visited[v] = 2

        for i in adj[v]:
            if visited[i] == 0:
                if visit(i) == False:
                    return False
            elif visited[i] == 2:
                return False

        visited[v] = 1

        return True

    visited = [0] * len(adj)

    for i in range(len(adj)):

        if not visited[i]:
            if visit(i) == False:
                return 1

    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
