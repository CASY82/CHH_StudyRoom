import sys

def min_adjust_cost(heights):
    if not heights:
        return 0

    best = float('inf')
    for L in range(0, 84):
        H = L + 17
        cost = 0
        for h in heights:
            if h < L:
                d = L - h
                cost += d * d
            elif h > H:
                d = h - H
                cost += d * d
        if cost < best:
            best = cost
    return best

n = int(sys.stdin.readline())
data = []

for _ in range(n):
    data.append(int(sys.stdin.readline()))

print(min_adjust_cost(data))