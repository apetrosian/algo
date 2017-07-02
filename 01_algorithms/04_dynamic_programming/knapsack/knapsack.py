# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    result = [[0 for x in range(W+1)] for y in range(len(w)+1)]

    for x in range(1, len(result)):
        # x = number of used bars

        for s in range(1, len(result[x])):
            # s = size of ks
            result[x][s] = result[x-1][s]

            if w[x-1] <= s:

                val = result[x-1][s-w[x-1]] + w[x-1]

                if result[x][s] <= val:
                    result[x][s] = val

        #print(result[x])

    # w = reversed(w)
    #
    # for x in w:
    #     if result + x <= W:
    #         result = result + x
    return result[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
