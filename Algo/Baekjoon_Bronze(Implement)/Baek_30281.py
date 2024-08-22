import sys

n = int(sys.stdin.readline())
candy = []
while True:
    try:
        candy += list(map(int, input().split()))
    except:
        break

min_odd = 999999
odd_cnt = 0

for i in range(len(candy)):
    if candy[i] % 2 == 1:
        odd_cnt += 1
        min_odd = min(candy[i], min_odd)

if odd_cnt % 2 == 0:
    print(sum(candy) // 2)
else:
    print((sum(candy) - min_odd) // 2)