import sys

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

# 경계처리를 위해 0 두 개 추가
A += [0, 0]

cost = 0

for i in range(N):
    # 1) (i+1) 쪽이 (i+2)보다 많으면 먼저 2묶음으로 줄여 균형 맞추기
    if A[i+1] > A[i+2]:
        pair = min(A[i], A[i+1] - A[i+2])
        A[i]   -= pair
        A[i+1] -= pair
        cost += 5 * pair

    # 2) 3연속 묶음 최대한 구매
    triple = min(A[i], A[i+1], A[i+2])
    if triple:
        A[i]   -= triple
        A[i+1] -= triple
        A[i+2] -= triple
        cost += 7 * triple

    # 3) 남은 만큼 2묶음 구매
    pair = min(A[i], A[i+1])
    if pair:
        A[i]   -= pair
        A[i+1] -= pair
        cost += 5 * pair

    # 4) 남은 건 단품
    if A[i]:
        cost += 3 * A[i]
        A[i] = 0

print(cost)
