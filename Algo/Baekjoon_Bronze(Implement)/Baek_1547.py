m = int(input())
cup = [0] * 4
cup[1] = 1

for _ in range(m):
    moved, moving = map(int, input().split())

    cup[moved], cup[moving] = cup[moving], cup[moved]



print(cup.index(1))
