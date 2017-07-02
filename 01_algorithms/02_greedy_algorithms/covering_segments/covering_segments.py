# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def in_segment(s, end):
    if end <= s.end and end >= s.start:
        return True
    else:
        return False


def get_min_end(segments):

    min = -1

    for s in segments:

        if min == -1:
            min = s.end

        if s.end < min:
            min = s.end

    return min

def optimal_points(segments):

    points = []

    while len(segments) > 0:

        min_end = get_min_end(segments)

        points.append(min_end)

        removed = []

        for s in segments:
            if in_segment(s, min_end):
                removed.append(s)

        for s in removed:
            segments.remove(s)

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
