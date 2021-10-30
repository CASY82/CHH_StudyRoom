t = int(input())

for _ in range(t):
    num = list(map(int, input().split()))
    even = []

    for i in num:
        if i % 2 == 0:
            even.append(i)

    even.sort()

    print(sum(even), min(even))