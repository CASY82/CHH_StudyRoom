import sys

n = int(sys.stdin.readline())
medicine = dict()

for _ in range(n):
    effect, name = map(int, sys.stdin.readline().split())
    medicine[effect] = name

case = int(sys.stdin.readline())

for _ in range(case):
    diseases = list(map(int, sys.stdin.readline().split()))
    result = []

    disease_cnt = diseases[0]
    diseases = diseases[1:]

    for disease in diseases:
        if disease in medicine:
            result.append(medicine[disease])

    if len(result) == disease_cnt:
        print(*result)
    else:
        print("YOU DIED")