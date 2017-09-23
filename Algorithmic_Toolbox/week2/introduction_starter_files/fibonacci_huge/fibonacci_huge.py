# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if m < 2:
       return 'Invalid Input'

    pisanoPeriod = []
    pisanoPeriod.append(0)
    pisanoPeriod.append(1)
    periodComplete = False

    for i in range(2,n+1):
        mod = (pisanoPeriod[i-1] + pisanoPeriod[i-2])%m

        if (mod == 1 and pisanoPeriod[i-1] == 0):
            pisanoPeriod.pop()
            periodComplete = True
            break
        else :
            pisanoPeriod.append(mod)

    if periodComplete:
        modindex = n%len(pisanoPeriod)
        return pisanoPeriod[modindex]
    else:
        return mod



if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
