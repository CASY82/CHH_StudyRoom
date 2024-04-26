import sys

n = int(sys.stdin.readline())

def div_pizza(pizza):
    if pizza == 1:
        return 0

    first = pizza // 2
    second = pizza - first

    tmp = first * second

    return tmp + div_pizza(first) + div_pizza(second)

print(div_pizza(n))

# 다른 사람 풀이
# N=int(input())
# print(N*~-N//2)