import sys

u, n = map(int, sys.stdin.readline().split())

price = [10001 for _ in range(10001)]
# people_list = dict()
people_list = [[] for _ in range(10001)]

for _ in range(n):
    name, suggest = sys.stdin.readline().strip().split()
    suggest = int(suggest)

    if price[suggest] >= 10001:
        price[suggest] = 1
    else:
        price[suggest] += 1

    people_list[suggest].append(name)

tmp = price.index(min(price))
print(people_list[tmp][0], tmp)