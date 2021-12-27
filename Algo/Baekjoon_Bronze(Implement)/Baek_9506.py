import sys

def perNum(n : int):
    num = []

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            num.append(i)
            num.append(n // i)

    num.sort()
    num.pop()

    return num

while True:
    n = int(sys.stdin.readline())

    if n == -1:
        break

    result = list(map(str, perNum(n)))

    if n == sum(perNum(n)):
        print(n, "=", ' + '.join(result))
    else:
        print(n, "is NOT perfect.")