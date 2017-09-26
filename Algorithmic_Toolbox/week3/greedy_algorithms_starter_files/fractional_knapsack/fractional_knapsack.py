# Uses python3
import sys
import operator

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.valuebyweight = value/weight

def itemsComparator(a,b):
    vaulebyweigthofa = a.value/a.weight
    vaulebyweigthofb = b.value/b.weight

    if (vaulebyweigthofa >= vaulebyweigthofb):
        return 1

    return -1

def get_optimal_value(capacity, weights, values):
    # write your code here
    value = 0
    items = []
    for i in range(0,len(weights)):
        items.append(Item(weights[i], values[i]))

    items.sort(key=operator.attrgetter('valuebyweight'), reverse=True)

    iterator = 0
    while(capacity > 0 and iterator < len(items)):
        fraction = min(capacity, items[iterator].weight)
        capacity = capacity - fraction
        value = value + (fraction * items[iterator].valuebyweight)
        iterator += 1
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values =  data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
