# Uses python3
import sys
from collections import namedtuple
import operator

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    # segments = [Segment(4,7), Segment(1,3), Segment(2,5), Segment(5,6)]
    #write your code here
    segments.sort(key=operator.attrgetter('start'))
    currentSegement = segments[0]
    iterator = 1
    while(True):
        if(iterator >= n):
            points.append(currentSegement.end)
            break

        mergedstart = max(currentSegement.start, segments[iterator].start)
        mergedend = min(currentSegement.end, segments[iterator].end)

        if (mergedstart <= mergedend):
            currentSegement = Segment(mergedstart, mergedend)
        else :
            points.append(mergedend)
            currentSegement = segments[iterator]

        iterator += 1
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
