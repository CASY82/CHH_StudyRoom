import sys

dish = sys.stdin.readline().strip()
result = 10

for i in range(1, len(dish)):
    if dish[i-1] != dish[i]:
        result += 10

    else:
        result += 5

print(result)