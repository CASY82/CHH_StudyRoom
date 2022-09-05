import sys

t = int(sys.stdin.readline())

for _ in range(t):
    susic = sys.stdin.readline().strip().split()

    tmp = "".join(susic[:-2])

    if int(susic[-1]) == eval(tmp):
        print("correct")
    else:
        print("wrong answer")