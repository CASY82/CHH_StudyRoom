import sys
import math

n = int(sys.stdin.readline())

tmp = math.factorial(n)
time = 7 * 24 * 60 * 60

print(tmp // time)