import sys

r, b = map(int, sys.stdin.readline().split())

total = r + b

for i in range(2, 5000):
    for j in range(2, 5000):
        if i * j == total:
            if 2 * i + 2 * j - 4 == r:
                print(max(i, j), min(i, j))
                exit()

# 다른 사람 풀이
# R, B = map(int, input().split())
#
# sum = R//2-2
#
# # 1부터 sum까지 돌면서 둘이 곱해서 B랑 같은지 확인
# for i in range(1,sum+1):
# 	if B==i*(sum-i):
# 		print(sum-i+2,i+2)
# 		break

# 다른 사람 풀이2
# R, B = map(int, input().split())
# if B == 1:
#     ans = R + B
#     print(int(ans**0.5), int(ans**0.5))
# else:
#     for i in range(1, int(B**0.5)+1):
#         if 2*i + 2*(B//i) + 4 == R and B % i == 0:
#             a, b = i+2, B//i + 2
#             break
#     if a >= b:
#         print(a, b)
#     else:
#         print(b, a)