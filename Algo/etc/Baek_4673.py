def selfnumber(n):
    tmp = n
    length = len(str(n))
    sum = n

    for i in range(length):
        sum += (tmp % 10)
        tmp = tmp // 10

    return sum

num = [False for i in range(10000)]

for i in range(1, 10000):
    if selfnumber(i) < 10000:
        num[selfnumber(i)] = True

for i in range(1, 10000):
    if not num[i]:
        print(i)