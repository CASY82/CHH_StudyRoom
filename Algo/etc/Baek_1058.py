#Floyd-Warshall을 활용해보았다.
n = int(input())
friend = []
counter = []

for i in range(n):
    friend.append(list(input()))

for k in range(n):
    people = [1 for i in range(n)]
    people[k] = 2

    for z in range(n):
        if friend[k][z] == 'Y':
            people[z] = 0

            for j in range(n):
                if friend[z][j] == 'Y':
                    people[j] = 0

    counter.append(people.count(0))

if max(counter) > 0:
    print(max(counter) - 1)
else:
    print(0)

#다른 사람 풀이 : 내가 푼거 보다 좀 더 깔끔하게 되어있다.
# n = int(input())
# friends = [list(map(str, input())) for _ in range(n)]
# graph = [[0 for _ in range(n)] for _ in range(n)]
# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 continue
#             elif friends[i][j] == 'Y':
#                 graph[i][j] = 1
#             elif friends[i][k] == 'Y' and friends[k][j] == 'Y':
#                 graph[i][j] = 1
# result = 0
# for gra in graph:
#     if result < sum(gra):
#         result = sum(gra)
# print(result)