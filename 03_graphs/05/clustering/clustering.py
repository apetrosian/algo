#Uses python3
import sys
import math

def build_graph(x, y, n):
    edges = [[] for i in range(n)]
    dist = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                edges[i].append(j)
                dist[i].append(calc_len(x[i], y[i], x[j], y[j]))
    return edges, dist

def calc_len(x1, y1, x2, y2):
    return math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))

def clustering(x, y, k):

    n = len(x)

    if n == 0:
        return 0

    edge, dist = build_graph(x, y, n)

    return -1.


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
