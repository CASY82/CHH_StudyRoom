import sys

n, k = map(int, sys.stdin.readline().split())
cnt = 0

k = str(k)
tmp = n * 3600 + 59 * 60 + 59

def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return hours, minutes, remaining_seconds

for i in range(tmp + 1):
    hour, minute, second = seconds_to_hms(i)

    if k in f"{hour:02d}{minute:02d}{second:02d}":
        cnt += 1

print(cnt)

# 다른 풀이
# # 입력 받기
# N, K = map(int, input().split())
#
# # 포함되는 시간의 개수를 세기 위한 변수
# count = 0
#
# # 모든 시간을 순회
# for h in range(N + 1):  # 시
#     for m in range(60):  # 분
#         for s in range(60):  # 초
#             # 시간, 분, 초를 문자열로 변환하여 합침
#             time = f"{h:02d}{m:02d}{s:02d}"
#             # 특정 숫자 K가 포함되어 있다면 카운트 증가
#             if str(K) in time:
#                 count += 1
#
# # 결과 출력
# print(count)
