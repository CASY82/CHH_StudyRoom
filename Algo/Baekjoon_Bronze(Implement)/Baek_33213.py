import sys

n = int(sys.stdin.readline())
shirts = list(map(int, sys.stdin.readline().split()))

def check(start, array):
    while True:
        if start not in array:
            return start

        start += 2

even = []
odd = []

for i in range(n):
    if shirts[i] % 2 == 0:
        even.append(shirts[i])
    else:
        odd.append(shirts[i])

if len(even) > len(odd):
    print(check(2, even))
else:
    print(check(1, odd))