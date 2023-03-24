import sys

hour, min = map(int, sys.stdin.readline().split())

change_min = (hour - 9) * 60

print(min + change_min)