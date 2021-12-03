t = int(input())

for _ in range(t):
    store = int(input())
    location = list(map(int, input().split()))

    location.sort()

    result = 0
    for i in range(len(location)-1):
        result += location[i+1]-location[i]

    print(result * 2)