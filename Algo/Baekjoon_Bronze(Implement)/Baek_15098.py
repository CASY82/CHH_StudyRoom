import sys

sentense = list(sys.stdin.readline().split())
check = set()
result = "yes"

for i in range(len(sentense)):
    if sentense[i] not in check:
        check.add(sentense[i])
    else:
        result = "no"
        break

print(result)