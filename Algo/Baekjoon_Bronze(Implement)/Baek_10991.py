import sys

n = int(sys.stdin.readline())

for i in range(n):
    tmp = n-1
    star = 0
    cnt = 0
    for j in range(2 * n - 1):
        if j == tmp + i - cnt:
            print("*", end='')
            star += 1
            if cnt < i:
                cnt -= 2
        elif j == tmp - i + cnt:
            print("*", end='')
            star += 1
            if cnt < i:
                cnt += 2
        else:
            print(" ", end='')

        if j == tmp:
            cnt -= 2

        if star == i+1:
            break

    print()

# 내가 많이 멍청하긴 한갑다.. 위에 코드 생각하는데 너무 오래걸림;;; 그와중에 코드도 너무 길어서...
# 아래는 참조 소스
# num = int(input())
#
# for line in range(1, num+1):
#     for _ in range(num - line):
#         print(' ', end='')
#     for _ in range(line):
#         print('* ', end='')
#     print()
