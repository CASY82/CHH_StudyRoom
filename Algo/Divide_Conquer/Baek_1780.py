import sys
sys.setrecursionlimit(300000)

n = int(sys.stdin.readline())
colorpaper = []
cnt = [0, 0, 0]

for _ in range(n):
    colorpaper.append(list(map(int, sys.stdin.readline().split())))

def dc(x, y, n):
    check = colorpaper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != colorpaper[i][j]:
                check = -2
                break

    if check == -2:
        n //= 3
        dc(x, y, n)
        dc(x, y + n, n)
        dc(x, y + (2 * n), n)
        dc(x + n, y, n)
        dc(x + n, y + n, n)
        dc(x + n, y + (2 * n), n)
        dc(x + (2 * n), y, n)
        dc(x + (2 * n), y + n, n)
        dc(x + (2 * n), y + (2 * n), n)

    elif check == -1:
        cnt[0] += 1
    elif check == 0:
        cnt[1] += 1
    else:
        cnt[2] += 1

dc(0, 0, n)
for view in cnt:
    print(view)

# 시간이 제일 적게 든 코드를 찾아보았다. 다른사람 코드 참고
# def count_papers(paper, n, x, y, result):
#     # 종이 전체가 같은 숫자로 이루어져 있는 경우
#     if n == 1:
#         result[paper[x][y] + 1] += 1
#         return
#
#     # 종이를 1/3으로 나누어서 각 부분이 같은 숫자로 이루어져 있는지 확인
#     same = True
#     for i in range(x, x + n):
#         for j in range(y, y + n):
#             if paper[i][j] != paper[x][y]:
#                 same = False
#                 break
#         if not same:
#             break
#
#     # 같은 숫자로 이루어져 있지 않다면 다시 1/3으로 나누어 재귀적으로 확인
#     if not same:
#         m = n // 3
#         for i in range(3):
#             for j in range(3):
#                 count_papers(paper, m, x + i * m, y + j * m, result)
#     else:
#         result[paper[x][y] + 1] += 1
#
#
# n = int(input())
# paper = []
# result = [0, 0, 0]  # 0: -1의 개수, 1: 0의 개수, 2: 1의 개수
# for i in range(n):
#     paper.append(list(map(int, input().split())))
#
# count_papers(paper, n, 0, 0, result)
#
# print(result[0])
# print(result[1])
# print(result[2])