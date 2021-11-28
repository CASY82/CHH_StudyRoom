# 생각해보니 result 배열을 따로 쓰지않고 바로 찍으면 되는 문제였던거 같다.

# n = int(input())
# result = []
# i = 2

# while n > 1:
#     if n % i == 0:
#         result.append(i)
#         n //= i
#         continue
#
#     i += 1
#
# result.sort()
#
# for i in result:
#     print(i)

# 그래서 줄여서 다시 제출해 보았다~

n = int(input())
i = 2

while n > 1:
    if n % i == 0:
        print(i)
        n //= i
        continue

    i += 1