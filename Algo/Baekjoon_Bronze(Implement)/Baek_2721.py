t = int(input())

def t_func(num):
    result = 0
    for i in range(1, num+1):
        result += i

    return result

for _ in range(t):
    n = int(input())
    sum = 0

    for i in range(1, n+1):
        sum += (i * t_func(i+1))

    print(sum)