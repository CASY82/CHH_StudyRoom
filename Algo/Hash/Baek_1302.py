import sys

n = int(sys.stdin.readline())
dic = dict()

for _ in range(n):
    book = sys.stdin.readline().strip()

    if not book in dic:
        dic[book] = 1
    else:
        dic[book] += 1

result = [k for k,v in dic.items() if max(dic.values()) == v]
result.sort()

print(result[0])