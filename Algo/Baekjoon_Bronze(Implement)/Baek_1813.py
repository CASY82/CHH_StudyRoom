#애매하게 맞춘 문제... 모순 이라는 개념에 대해서 헷갈리고 있는 모양이다.
n = int(input())
num = [int(x) for x in input().strip().split()]
result = -1

for i in range(max(num) + 1):
    if num.count(i) == i:
        if result < i:
            result = i

print(result)