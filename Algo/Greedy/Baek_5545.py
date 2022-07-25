import sys

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())

toping = []


for _ in range(n):
    toping.append(int(sys.stdin.readline()))

toping.sort(reverse=True)

best_pizza = c // a
k = 1
cal = c

while True:
    cal += toping[k-1]

    now_pizza = cal // (a + b * k)

    if best_pizza < now_pizza:
        best_pizza = now_pizza

    if k >= n:
        break

    k += 1

print(best_pizza)