import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

# 1. 완성된 문자에서 A로 끝나는지 B로 끝나는지 판별
# 2. 완성된 문자에서 2가지 방법을 거꾸로 적용하여 원래 시작 문자가 만들어지는 확인

while len(t) > len(s):
    if t[-1] == 'A':
        t = t[:len(t) - 1]
    else:
        t = t[:len(t) - 1]
        t = t[::-1]

if t == s:
    print(1)
else:
    print(0)