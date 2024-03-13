import sys

n, k = map(int, sys.stdin.readline().split())
score = list(map(int, sys.stdin.readline().split()))

def grade(n):
    if 0 <= n <= 4:
        return 1
    elif 4 < n <= 11:
        return 2
    elif 11 < n <= 23:
        return 3
    elif 23 < n <= 40:
        return 4
    elif 40 < n <= 60:
        return 5
    elif 60 < n <= 77:
        return 6
    elif 77 < n <= 89:
        return 7
    elif 89 < n <= 96:
        return 8
    elif 96 < n <= 100:
        return 9

for i in range(k):
    if i < k - 1:
        print(grade(score[i] * 100 // n), end=" ")
    else:
        print(grade(score[i] * 100 // n), end="")