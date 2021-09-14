l, p = map(int, input().split())

article = list(map(int, input().split()))

for i in article:
    print(i - (p * l), end=' ')