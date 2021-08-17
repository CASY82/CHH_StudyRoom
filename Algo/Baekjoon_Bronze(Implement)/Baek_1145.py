import math
from itertools import permutations

num_list = list(map(int, input().split()))
#5개의 수가 고정이므로 5개 중 3개를 선택하는 모든 경우의 수를 구한다.
com_tuple = list(permutations(num_list, 3))
com_list = []
result = []

#3개의 수의 최소 공배수 구하기(두 수의 곱 / 두 수 최대 공약수의 곱)
def lcm(first, second, third):
    fir_lcm = (first * second) // math.gcd(first, second)
    sec_lcm = (second * third) // math.gcd(second, third)

    return (fir_lcm * sec_lcm) // math.gcd(fir_lcm, sec_lcm)

for i in com_tuple:
    com_list.append(list(i))

for i in range(len(com_list)):
    result.append(lcm(com_list[i][0], com_list[i][1], com_list[i][2]))

result.sort()

print(result[0])

#제일 작은 수 부터 시작해서 약수가 3개 이상이 될 때 까지 계속 반복문을 돌린다. 위 방법으로 통과는 했으나 너무 무식했다.
# li = list(map(int, input().split()))
#
# n = min(li)
# while 1:
#     cnt = 0
#     for i in li:
#         if n % i == 0:
#             cnt += 1
#     if cnt > 2:
#         break
#     n += 1
# print(n)