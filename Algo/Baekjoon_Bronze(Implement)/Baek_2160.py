n = int(input())
picture = []
counter = []

for i in range(n):
    pic = []
    for j in range(5):
        pic.append(list(input()))


    picture.append(pic)

for i in range(len(picture)):
    for j in range(i+1, len(picture)):
        count = 0
        for a in range(5):
            for b in range(7):
                if picture[i][a][b] != picture[j][a][b]:
                    count += 1

        counter.append([count, i+1, j+1])

print(min(counter)[1], min(counter)[2])


#다른사람 풀이 참고
#
# def compare(i,j):
#     result = 0
#     for a in range(5):
#         for b in range(7):
#             if pic[i][a][b] != pic[j][a][b]:
#                 result += 1
#     return result
#
#
# n = int(input())
# pic = [[input() for _ in range(5)] for _ in range(n)]
#
# min_cnt = float('inf')
#
# for i in range(n-1):
#     for j in range(i+1,n):
#         current_cnt = compare(i,j)
#         if current_cnt < min_cnt:
#             min_cnt = current_cnt
#             idx = [i+1,j+1]
#
# print(*idx)