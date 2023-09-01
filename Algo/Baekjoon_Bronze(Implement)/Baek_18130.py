import sys

n, q = map(int, sys.stdin.readline().split())

result = []

for i in range(n):
    p, k, c = map(int, sys.stdin.readline().split())

    additional_fee = 0

    if q // k == 1 and q % k != 0:
        additional_fee = 1
    elif q // k != 0 and q % k != 0:
        additional_fee = (q // k) * ((q // k) + 1) // 2
    elif q // k != 0 and q % k == 0:
        additional_fee = (q // k) * ((q // k) - 1) // 2

    tmp = p + additional_fee * c

    result.append((i+1, tmp))

result.sort(key=lambda x: (x[1], x[0]))

print(result[0][0], result[0][1])