import sys

kanpan = sys.stdin.readline().strip()

correct = "UAPC"
res = ""

for i in range(4):
    if correct[i] not in kanpan:
        res += correct[i]

print(res)