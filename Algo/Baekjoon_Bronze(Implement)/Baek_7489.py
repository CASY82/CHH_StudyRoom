t = int(input())

for _ in range(t):
    n = int(input())

    result = 1
    for i in range(1, n+1):
        result *= i

        while True:
            if result % 10 == 0:
                result //= 10
            else:
                break

    print(result%10)