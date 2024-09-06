import sys

n = int(sys.stdin.readline())
swifts = list(map(int, sys.stdin.readline().split()))
semaphores = list(map(int, sys.stdin.readline().split()))

res = 0

swifts_sum = 0
semaphores_sum = 0

for i in range(n):
    swifts_sum += swifts[i]
    semaphores_sum += semaphores[i]

    if semaphores_sum == swifts_sum:
        res = i + 1

print(res)