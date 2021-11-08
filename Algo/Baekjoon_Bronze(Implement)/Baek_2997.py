num = list(map(int, input().split()))

num.sort()

if num[1] - num[0] == num[2] - num[1]:
    print(num[0] + (3 * (num[1] - num[0])))
elif (num[1] - num[0]) * 2 == num[2] - num[1]:
    print(num[0] + (2 * (num[1] - num[0])))
elif num[1] - num[0] == (num[2] - num[1]) * 2:
    print(num[0] + (num[2] - num[1]))