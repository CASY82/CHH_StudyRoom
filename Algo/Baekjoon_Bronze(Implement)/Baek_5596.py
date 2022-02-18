import sys

minkuk = list(map(int, sys.stdin.readline().split()))
mansae = list(map(int, sys.stdin.readline().split()))

print(max(sum(minkuk), sum(mansae)))