#Uses python3

import sys
import functools

def largest_number(a):
    #write your code here
    res = ''
    a.sort(key=functools.cmp_to_key(getmaxnumber), reverse=True)
    for number in a:
        res += str(number)
    return res

def getmaxnumber(a, b):
    awithb = int(str(a)+str(b))
    bwitha = int(str(b)+str(a))
    if (awithb >= bwitha):
        return 1
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
