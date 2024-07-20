import sys

n = int(sys.stdin.readline())
potato = list(map(int, sys.stdin.readline().split()))

potato.sort()

print(sum(potato[:len(potato) // 2]), sum(potato[len(potato) // 2:]))