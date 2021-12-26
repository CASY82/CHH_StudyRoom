import sys

t = int(sys.stdin.readline())
y_result = 0
k_result = 0

for _ in range(t):
    for _ in range(9):
        yonsei, korea = map(int, sys.stdin.readline().split())

        y_result += yonsei
        k_result += korea

    if y_result > k_result:
        print("Yonsei")
    elif y_result < k_result:
        print("Korea")
    else:
        print("Draw")