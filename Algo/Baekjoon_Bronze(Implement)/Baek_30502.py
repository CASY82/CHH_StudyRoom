import sys

n, m = map(int, sys.stdin.readline().split())

#0 운동성 / 1 광합성
bio = [[-1, -1] for _ in range(n)]

for _ in range(m):
    a, b, c = sys.stdin.readline().strip().split()

    a = int(a)

    if b == "M":
        bio[a - 1][0] = int(c)

    if b == "P":
        bio[a - 1][1] = int(c)

max_cnt = 0
min_cnt = 0

for i in range(n):
    if bio[i][0] != 1 and bio[i][1] != 0:
        max_cnt += 1
        if bio[i][1] == 1 and bio[i][0] == 0:
            min_cnt += 1

print(min_cnt, max_cnt)

# import sys
#
#
# def main():
#     input = sys.stdin.readline  # 빠른 입력을 위해
#     N, M = map(int, input().split())
#     v = [[-1, -1] for _ in range(N + 1)]  # 0: 광합성, 1: 운동성
#
#     for _ in range(M):
#         a, b, c = input().strip().split()
#         a = int(a)
#         c = int(c)
#
#         if b == 'P':  # 광합성인 경우
#             v[a][0] = c
#         else:  # 운동성인 경우
#             v[a][1] = c
#
#     min_count = 0
#     max_count = 0
#
#     for i in range(1, N + 1):
#         if v[i][0] != 0 and v[i][1] != 1:  # 광합성을 하지 않는 경우가 아니면서 운동성이 있는 경우가 아닌 것
#             max_count += 1
#             if v[i][0] == 1 and v[i][1] == 0:  # 광합성을 하고 운동성이 없는 경우
#                 min_count += 1
#
#     print(min_count, max_count)
#
#
# if __name__ == "__main__":
#     main()
