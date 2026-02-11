# 숭고한에 어서오세요
import sys

n = int(sys.stdin.readline())
years = list(map(int, sys.stdin.readline().split()))

diff = years[1] - years[0]

print(years[-1] + diff)