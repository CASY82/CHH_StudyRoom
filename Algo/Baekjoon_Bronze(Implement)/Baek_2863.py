a, b = map(int, input().split())
c, d = map(int, input().split())

result = []

for i in range(4):
    result.append((a / c) + (b / d))
    a, b, c, d = c, a, d, b

print(result.index(max(result)))