import sys
import itertools

n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
tmp = set()

for i in range(1, len(str(n)) + 1):
    combinations = itertools.product(nums, repeat=i)

    for comb in combinations:
        num = int("".join(map(str, comb)))
        if num <= n:
            tmp.add(num)

tmp = list(tmp)

print(max(tmp))

#
# import sys
# import itertools
#
# # 입력 받기
# n, k = map(int, sys.stdin.readline().split())
# nums = list(map(int, sys.stdin.readline().split()))
#
# # N의 길이를 계산
# n_str = str(n)
# n_len = len(n_str)
#
# # 가능한 수를 저장할 리스트
# possible_numbers = []
#
# # 1자리부터 n_len 자리까지 가능한 모든 경우를 확인
# for i in range(1, n_len + 1):
#     # itertools.product를 이용하여 i자리 수를 만든다
#     for comb in itertools.product(nums, repeat=i):
#         number = int("".join(map(str, comb)))
#         if number <= n:
#             possible_numbers.append(number)
#
# # 가능한 수 중에서 가장 큰 수를 출력
# print(max(possible_numbers))

# 다른사람 풀이
#
# import sys
#
#
# def recursive():
#     global N_len, ans, max_ans, N
#     for k in KK:
#         ans.append(str(k))
#         if len(ans) < N_len:
#             recursive()
#
#         ans_num = int(''.join(ans))
#         if ans_num <= N:
#             max_ans = max(max_ans, ans_num)
#         ans.pop()
#
#
# if __name__ == '__main__':
#     N, K = map(int, sys.stdin.readline().rstrip().split())
#     KK = list(map(int, sys.stdin.readline().rstrip().split()))
#
#     N_len = len(str(N))
#     ans = list()
#     max_ans = -1
#
#     recursive()
#
#     print(max_ans)