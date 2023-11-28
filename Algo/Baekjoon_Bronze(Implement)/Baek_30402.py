import sys

cat = []

for _ in range(15):
    tmp = list(sys.stdin.readline().strip().split())

    if "w" in tmp:
        print("chunbae")
        break
    elif "b" in tmp:
        print("nabi")
        break
    elif "g" in tmp:
        print("yeongcheol")
        break