import sys

s = int(sys.stdin.readline())

i = 1
while True:
    right = (i + 1) * i // 2
    left = i * (i - 1) // 2
    if s >= (left-1) and s <= (right-1):
        break

    i += 1

print(i - 1)

#더 짧게 짤수 있었다...
# s = int(input())
# n = 1
# while n * (n + 1) / 2 <= s:
#     n += 1
# print(n - 1)