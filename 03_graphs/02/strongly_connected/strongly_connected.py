#Uses python3

import sys

sys.setrecursionlimit(200000)

def number_of_strongly_connected_components(adj):
    result = 0

    n = len(adj)

    post_order = []

    reverse = [[] for _ in range(n)]

    # reverse graph
    for i in range(n):
        for j in range(len(adj[i])):
            reverse[ adj[i][j] ].append(i)


    def dfs(v):
        visited[v] = 1

        for i in reverse[v]:
            if not visited[i]:
                dfs(i)

        post_order.insert(0, v)

    def explore(v, res):

        visited[v] = res

        for i in adj[v]:
            if not visited[i]:
                explore(i, res)

    visited = [0] * n

    # run dfs in reverse postorder
    for i in range(n):

        if not visited[i]:
            dfs(i)

    visited = [0] * n

    #print(post_order)

    for i in post_order:

        if not visited[i]:
            result += 1
            explore(i, result)

    #print(visited)

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
