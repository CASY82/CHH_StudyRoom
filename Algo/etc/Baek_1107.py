import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

if m != 0:
    broken_button = set(input().split())
else:
    broken_button = set()

def check(num):
    for ch in str(num):
        if ch in broken_button:
            return False
    return True

min_press = abs(n - 100)

for i in range(1000000):
    if check(i):
        press = len(str(i)) + abs(n - i)
        min_press = min(min_press, press)

print(min_press)

# N = int(input())  # 목표 채널
# M = int(input())  # 고장난 버튼 수
#
# if M:
#     broken = set(input().split())
# else:
#     broken = set()
#
# def can_press(num):
#     for digit in str(num):
#         if digit in broken:
#             return False
#     return True
#
# # 1. +, - 버튼만 사용하는 경우
# min_press = abs(N - 100)
#
# # 2. 숫자 버튼 + 이동을 사용하는 경우
# for cand in range(1000000):  # 최대 6자리 채널까지 확인
#     if can_press(cand):
#         press_count = len(str(cand)) + abs(cand - N)
#         min_press = min(min_press, press_count)
#
# print(min_press)
