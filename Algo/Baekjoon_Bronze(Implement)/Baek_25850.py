# A Game Called Mind
import sys

player = ["A", "B", "C", "D", "E", "F"]

n = int(sys.stdin.readline())
array = []

for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    array = array + [(val, player[i]) for val in tmp[1:]]

array.sort(key=lambda x:x[0])

for i in range(len(array)):
    print(array[i][1], end="")