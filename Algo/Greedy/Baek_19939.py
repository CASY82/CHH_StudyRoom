import sys

n, k = map(int, sys.stdin.readline().split())
bucket = [1] * k

# 1. 바구니는 비어있으면 안됨
# 2. 각 바구니의 공이 같아도 안되므로 "="포함
if n <= k:
    print(-1)
else:
    n -= k
    cnt = 0
    #공 분배
    while n > 0:
        if cnt < k:
            cnt += 1
        for i in range(cnt):
            bucket[i] += 1
            n -= 1
            if n == 0:
                break

    #개수 같은지 다시 확인
    check = True
    for i in range(max(bucket)):
        if bucket.count(i) >= 2:
            check = False
            break

    if check:
        print(max(bucket) - min(bucket))
    else:
        print(-1)

#역시 수학으로 푸는 방법이 있을줄 알았다...
# N, K = map(int, input().split())
#
# if N < K*(K+1)/2:
#   print(-1)
# else:
#   if (N-K*(K+1)/2)%K == 0:
#     print(K-1)
#   else:
#     print(K)