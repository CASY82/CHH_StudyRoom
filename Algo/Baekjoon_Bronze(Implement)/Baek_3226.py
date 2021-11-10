n = int(input())
result = 0

for _ in range(n):
    time, using = input().split()

    using = int(using)
    time_check = list(time.split(':'))
    time_check[0] = int(time_check[0])
    time_check[1] = int(time_check[1])


    if time_check[0] == 6:
        if time_check[1] + using >= 60:
            result += abs(60 - time_check[1]) * 5 + abs(using - (60 - time_check[1])) * 10
        else:
            result += using * 5
    elif time_check[0] == 18:
        if time_check[1] + using >= 60:
            result += abs(60 - time_check[1]) * 10 + abs(using - (60 - time_check[1])) * 5
        else:
            result += using * 10
    else:
        if time_check[0] >= 7 and time_check[0] < 18:
            result += using * 10
        else:
            result += using * 5

print(result)