import sys

n = int(sys.stdin.readline())
# numList = []

cnt = 0

for i in range(3, n+1, 3):
    for j in range(3, n-i+1, 3):
        if n - i - j <= 0:
            continue
        #이거 빼도되는데 ㅋ
        # numList.append([i,j,n-i-j])
        cnt += 1

print(cnt)