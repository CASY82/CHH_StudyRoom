a, b, c = map(int, input().split())

if b < c:
    print(int(abs(a / (b - c)) + 1))
else:
    print(-1)