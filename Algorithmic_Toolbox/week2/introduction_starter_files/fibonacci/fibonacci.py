# Uses python3
def calc_fib(n):
    if n <= 1:
        return n

    fibtable = []
    fibtable.append(1) #0
    fibtable.append(1) #1

    for i in range(2,n):
        fibtable.append(fibtable[i-1]+fibtable[i-2])

    return fibtable[n-1]

n = int(input())
print(calc_fib(n))
