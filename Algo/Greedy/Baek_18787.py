import sys

n = int(sys.stdin.readline())
origin = list(sys.stdin.readline().strip())
goal = list(sys.stdin.readline().strip())

continue_interval = []
cnt = 1

def count_isolated_zeros(arr):
    isolated_count = 0
    in_zero_sequence = False

    for num in arr:
        if num == 0:
            if not in_zero_sequence:
                # 0의 연속이 시작될 때 카운트
                isolated_count += 1
                in_zero_sequence = True
        else:
            in_zero_sequence = False  # 0의 연속이 끝났음을 표시

    return isolated_count


# 연속된 부분의 구간을 인덱스로 확인
for i in range(n):
    if goal[i] == origin[i]:
        cnt += 1
    else:
        cnt = 0

    continue_interval.append(cnt)

print(count_isolated_zeros(continue_interval))

# 다른 사람 풀이
# N = int(input())
# A = input()
# B = input()
#
#
# ans = 0
# for i in range(N):
#     if A[i] != B[i]:
#         if i == N-1:
#             ans += 1
#         elif A[i+1] == B[i+1]:
#             ans += 1
#
#
# print(ans)
