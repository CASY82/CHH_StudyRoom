# import sys
# import itertools
#
# n, k = map(int, sys.stdin.readline().split())
# nums = list(map(int, sys.stdin.readline().split()))
#
# combinations = itertools.product(nums, repeat=len(str(n)))
# tmp = set()
#
# for comb in combinations:
#     tmp.add(int("".join(map(str, comb))))
#
# combinations2 = itertools.product(nums, repeat=len(str(n)) - 1)
#
# for comb2 in combinations2:
#     tmp.add(int("".join(map(str, comb2))))
#
# tmp = list(tmp)
# tmp.sort()
#
# for i in range(len(tmp)):
#     if tmp[i] > n:
#         print(tmp[i - 1])
#         break
#     elif tmp[i] == n:
#         print(n)
#         break


import sys
import itertools

# 입력 받기
n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

# N의 길이를 계산
n_str = str(n)
n_len = len(n_str)

# 가능한 수를 저장할 리스트
possible_numbers = []

# 1자리부터 n_len 자리까지 가능한 모든 경우를 확인
for i in range(1, n_len + 1):
    # itertools.product를 이용하여 i자리 수를 만든다
    for comb in itertools.product(nums, repeat=i):
        number = int("".join(map(str, comb)))
        if number <= n:
            possible_numbers.append(number)

print(possible_numbers)

# 가능한 수 중에서 가장 큰 수를 출력
print(max(possible_numbers))
