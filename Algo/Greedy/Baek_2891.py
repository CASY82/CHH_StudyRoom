import sys

n, s, r = map(int, sys.stdin.readline().split())
lost = list(map(int, sys.stdin.readline().split()))
adder = list(map(int, sys.stdin.readline().split()))
kayak = [True] * n

# 1. 카약 손상팀과 카약 여분 팀을 비교하여 여분팀이 손상팀에 있는경우 여분과 손상 제거
for i in range(len(adder)-1, -1, -1):
    if adder[i] in lost:
        lost.remove(adder[i])
        adder.remove(adder[i])

# 2. 카약 손상팀이 카약 여분팀과 근접한지 확인
result = len(lost)

for i in adder:
    if i-1 in lost or i+1 in lost:
        result -= 1

if result <= 0:
    result = 0

print(result)