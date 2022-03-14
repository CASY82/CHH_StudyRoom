import sys

n = int(sys.stdin.readline())

for _ in range(n):
    sick = sys.stdin.readline().strip()

    if sick == "P=NP":
        print("skipped")
    else:
        print(eval(sick))