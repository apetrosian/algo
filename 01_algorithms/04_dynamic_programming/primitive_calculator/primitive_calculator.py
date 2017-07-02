# Uses python3


def optimal_sequence(n):

    sequence = []

    steps = [1]

    for i in range(1, n+1):

        best = steps[i-1]+1

        if i % 2 == 0:
            best = min(best, steps[i // 2] + 1)

        if i % 3 == 0:
            best = min(best, steps[i // 3] + 1)

        steps.append(best)

    #print(steps)

    while n > 1:
        sequence.append(n)

        if steps[n-1] == steps[n]-1:
            n = n - 1
        elif n % 2 == 0 and steps[n // 2] == steps[n]-1:
            n = n // 2
        elif n % 3 == 0 and steps[n // 3] == steps[n]-1:
            n = n // 3

    sequence.append(1)

    return reversed(sequence)

n = int(input())
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
