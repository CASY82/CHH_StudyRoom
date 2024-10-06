N = int(input())
A = list(map(int, input().split()))

min_diff = abs(A[1] - A[0])

for i in range(N - 1):
    if abs(A[i + 1] - A[i]) <= min_diff:
        min_diff = abs(A[i + 1] - A[i])

print(min_diff)