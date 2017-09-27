# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    minlimit = 1
    while(n > 0):
        summand = find_summands(n, minlimit)
        summands.append(summand)
        n -= summand
        minlimit += 1

    return summands

def find_summands(value, minsummand):
    if (value <= (2*minsummand)):
        return value
    else:
        return minsummand

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
