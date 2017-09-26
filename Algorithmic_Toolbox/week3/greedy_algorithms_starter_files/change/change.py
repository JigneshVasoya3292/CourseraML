# Uses python3
import sys

def get_change(m):
    #write your code here
    denomination = [10, 5, 1]
    coins = 0
    i = 0

    while(m >= 0 and i < len(denomination)):
        if (denomination[i] <= m):
            quantity = int(m/denomination[i])
            coins += quantity
            m -= quantity*denomination[i]
        i += 1

    return coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
