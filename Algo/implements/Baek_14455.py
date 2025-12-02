# import sys
#
# n = int(sys.stdin.readline())
# cow = dict()
#
# for _ in range(n):
#     name, milk = sys.stdin.readline().strip().split()
#
#     milk = int(milk)
#
#     cow[name] = cow.get(name, 0) + milk
#
# result = sorted(cow.items(), key=lambda x: x[1])
# low_milk = result[0][1]
#
# second_milk = None
# for name, milk in result:
#     if milk > low_milk:
#         second_milk = milk
#         break
#
# if second_milk is None:
#     print("Tie")
# else:
#     candidates = [name for name, milk in result if milk == second_milk]
#     if len(candidates) == 1:
#         print(candidates[0])
#     else:
#         print("Tie")

import sys

n = int(sys.stdin.readline())

names = ["Bessie", "Elsie", "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta"]
cow = {name: 0 for name in names}  # 모든 소를 0으로 초기화

for _ in range(n):
    name, milk = sys.stdin.readline().strip().split()
    milk = int(milk)
    cow[name] += milk

# 총 생산량 기준 오름차순 정렬
result = sorted(cow.items(), key=lambda x: x[1])

# 최소 생산량 M
low_milk = result[0][1]

# M보다 큰 값 중 최소값(second_min)을 찾음
second_min = None
for name, milk in result:
    if milk > low_milk:
        second_min = milk
        break

# M보다 큰 값이 아예 없으면(=모든 소가 같은 양) Tie
if second_min is None:
    print("Tie")
else:
    # second_min을 가진 소가 몇 마리인지 확인
    candidates = [name for name, milk in result if milk == second_min]
    if len(candidates) == 1:
        print(candidates[0])
    else:
        print("Tie")
