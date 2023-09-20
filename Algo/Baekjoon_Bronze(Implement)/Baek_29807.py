import sys

t = int(sys.stdin.readline())

# 국, 수, 영, 탐, 제2외국어
subject = list(map(int, sys.stdin.readline().split()))

if len(subject) < 5:
    tmp = 5 - len(subject)
    for _ in range(tmp):
        subject.append(0)

first = 0
second = 0
third = 0

if subject[0] > subject[2]:
    first = abs(subject[0] - subject[2]) * 508
else:
    first = abs(subject[0] - subject[2]) * 108

if subject[1] > subject[3]:
    second = abs(subject[1] - subject[3]) * 212
else:
    second = abs(subject[1] - subject[3]) * 305

if subject[-1] > 0:
    third = subject[-1] * 707

result = (first + second + third) * 4763

print(result)