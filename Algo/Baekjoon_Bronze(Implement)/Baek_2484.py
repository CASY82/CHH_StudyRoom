n = int(input())
result = []

for _ in range(n):
    dice = list(map(int, input().split()))

    dice.sort()

    if len(set(dice)) == 1:
        result.append(50000 + (dice[0] * 5000))
    elif len(set(dice)) == 2:
        for i in set(dice):
            if dice.count(i) == 2:
                result.append((dice[1] * 500) + (dice[2] * 500) + 2000)
            if dice.count(i) == 3:
                result.append((dice[1] * 1000) + 10000)

    elif len(set(dice)) == 3:
        for i in set(dice):
            if dice.count(i) == 2:
                tmp = i

        result.append((tmp * 100) + 1000)
    else:
        result.append(max(dice) * 100)

print(max(result))

'''
1
3 2 1 2
답:1200
'''