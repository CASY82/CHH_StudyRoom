import sys

input = sys.stdin.readline

N = int(input().strip())
digits = input().strip()

# 자릿수(0~9) 카운팅으로 O(N) 정렬
cnt = [0]*10
for ch in digits:
    cnt[ord(ch)-48] += 1

a = []
b = []
# 더 짧은 쪽에 작은 숫자부터 배치
for d in range(10):
    c = cnt[d]
    while c > 0:
        if len(a) <= len(b):
            a.append(str(d))
        else:
            b.append(str(d))
        c -= 1

# 문자열 -> 정수로 합 계산 (선행 0 허용)
A = int(''.join(a)) if a else 0
B = int(''.join(b)) if b else 0
print(A + B)
