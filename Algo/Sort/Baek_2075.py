import sys

n = int(sys.stdin.readline())

array = []

for _ in range(n):
    array += list(map(int, sys.stdin.readline().split()))
    array.sort()
    array = array[-n:]

print(array[0])