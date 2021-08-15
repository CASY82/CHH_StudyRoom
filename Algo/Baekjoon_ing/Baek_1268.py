# 코드 틀림... 반례를 못찾겠다.
# from sys import stdin
#
# student = int(stdin.readline())
# years = []
# same_class = [0 for _ in range(student)]
#
# for _ in range(student):
#     years.append(list(map(int, input().split())))
#
# for i in range(5):
#     for j in range(student):
#         for k in range((j + 1), student):
#             if years[j][i] == years[k][i]:
#                 same_class[j] += 1
#                 same_class[k] += 1
#
# print(same_class.index(max(same_class)) + 1)



#다른 사람 풀이 참고

N = int(input())
classes = [list(map(int, input().split())) for _ in range(N)]
cnt = [0]*N

for n in range(N):
    visited = [False for _ in range(N)]
    for grade in range(5):
        for student_id in range(N):
            if student_id != n and classes[student_id][grade] == classes[n][grade]:
                visited[student_id] = True
    cnt[n] = len(list(filter(lambda x: x, visited)))

print(visited)
print(cnt)

print(cnt.index(max(cnt))+1)


