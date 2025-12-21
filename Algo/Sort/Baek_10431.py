import sys

P = int(sys.stdin.readline().strip())

def count_shifts(heights):
    line = []
    shifts = 0
    for h in heights:
        idx = 0
        while idx < len(line) and line[idx] < h:
            idx += 1

        shifts += len(line) - idx
        line.insert(idx, h)
    return shifts

for _ in range(P):
    data = list(map(int, input().split()))
    T = data[0]
    heights = data[1:]
    print(T, count_shifts(heights))