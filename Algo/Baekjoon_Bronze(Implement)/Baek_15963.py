import sys

song, teacher = map(int, sys.stdin.readline().split())

if song == teacher:
    print(1)
else:
    print(0)