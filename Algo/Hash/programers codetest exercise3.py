# 해시 3번 위장

#[["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
#[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
#[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"], ["blacksunglasses", "eyewear"], ["smoky_makeup", "face"]]

from collections import Counter

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"], ["blacksunglasses", "eyewear"], ["smoky_makeup", "face"]]

# def solution(clothes):
#     count = 0
#     clothes.sort(key=lambda x:x[1])
#
#     for i in range(len(clothes)):
#         for j in range(len(clothes)):
#             if clothes[i][1] == clothes[j][1]:
#                 break
#
#             count += 1
#
#     return count+len(clothes)

#for문의 새로운 사용 방법을 익혔다!
var = [cat for _, cat in clothes]
print(var)


# 요점은 수학 공식을 이용한 풀이 경우의 수 (모자 개수 + 1) * (옷 개수 + 1) ... 를 한 뒤 마지막에 전부 안입은 경우 1을 빼서 구하는 것
def solution(clothes):
    counter_each_category = Counter([cat for _, cat in clothes])
    all_possible = 1

    for key in counter_each_category:
        all_possible *= (counter_each_category[key] + 1)

    return all_possible - 1

print(solution(clothes))