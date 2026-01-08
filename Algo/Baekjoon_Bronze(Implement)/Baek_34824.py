# 연대 다음 고대
import sys

n = int(sys.stdin.readline())
y_index = 9999

for i in range(n):
    name = sys.stdin.readline().strip()

    if name == "yonsei":
        y_index = i
    elif name == "korea":
        if y_index > i:
            print("Yonsei Lost...")
            break
        else:
            print("Yonsei Won!")
            break