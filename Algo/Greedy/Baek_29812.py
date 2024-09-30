# 뭔가 반례가 있는듯 안됨
# import sys
#
# n = int(sys.stdin.readline())
# s = sys.stdin.readline().strip()
# d, m = map(int, sys.stdin.readline().split())
#
# hyu_dict = {
#     "H": 0,
#     "Y": 0,
#     "U": 0
# }
#
# intervals = []
# current_interval = []
#
# for char in s:
#     if char not in "HYU":
#         current_interval.append(char)
#     else:
#         if current_interval:
#             intervals.append(''.join(current_interval))
#             current_interval = []
#
#         hyu_dict[char] += 1
#
# if current_interval:
#     intervals.append(''.join(current_interval))
#
# tmp = 0
# for st in intervals:
#     if len(st) > 1:
#         tmp += 1
#
# tmp_str_len = 0
#
# for s in intervals:
#     tmp_str_len += len(s)
#
# total = min(len(intervals) * d + tmp * m, tmp_str_len * d)
#
# if total == 0:
#     res_energy = 'Nalmeok'
# else:
#     res_energy = total
#
# if min(hyu_dict["H"], hyu_dict["Y"], hyu_dict["U"]) == 0:
#     res_hyu = 'I love HanYang University'
# else:
#     res_hyu = min(hyu_dict["H"], hyu_dict["Y"], hyu_dict["U"])
#
# print(res_energy)
# print(res_hyu)

import sys

# 입력을 처리합니다.
N = int(sys.stdin.readline())  # 문자열의 길이
s = sys.stdin.readline().strip()  # 입력된 문자열
D, M = map(int, sys.stdin.readline().split())  # delete와 drag의 에너지 비용

# 각 문자의 개수를 저장할 딕셔너리
cnt = {"H": 0, "Y": 0, "U": 0}

# 에너지 계산 변수
combo = 0
ans = 0

# 문자열을 순회하며 'H', 'Y', 'U'가 아닌 문자의 연속 구간의 길이를 combo로 계산합니다.
for l in s:
    if l == 'H' or l == 'Y' or l == 'U':
        # 현재 문자가 'H', 'Y', 'U'라면 해당 문자의 개수를 증가시킵니다.
        cnt[l] += 1
        # 지금까지 모아놓은 "HYU가 아닌 문자"의 연속된 길이(combo)를 바탕으로 에너지를 계산합니다.
        ans += min(M + D, combo * D)
        combo = 0  # combo를 초기화하여 새로운 구간을 추적합니다.
    else:
        combo += 1  # "HYU가 아닌 문자"의 길이를 증가시킵니다.

# 문자열을 모두 순회한 후 마지막으로 남은 "HYU가 아닌 문자" 구간을 에너지 계산에 반영합니다.
ans += min(M + D, combo * D)

# 에너지를 출력합니다.
if ans:
    print(ans)
else:
    print("Nalmeok")

# 'H', 'Y', 'U'의 최소 개수로 만들 수 있는 'HYU'의 개수를 계산합니다.
hyu_count = min(cnt['H'], cnt['Y'], cnt['U'])
if hyu_count:
    print(hyu_count)
else:
    print("I love HanYang University")
