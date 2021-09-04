n, q = map(int, input().split())
music_time = []
question = []
music_sum = []
val = 0

for i in range(n):
    music_time.append(int(input()))

for j in range(q):
    question.append(int(input()))

#위에서 합칠수 있지만 일단 냅둔다.
for k in range(n):
    val += music_time[k]
    music_sum.append(val)

for i in question:
    for j in range(len(music_sum)-1):
         if music_sum[j] <= i and music_sum[j + 1] > i:
             print(j+2)
             break
         elif i < music_sum[0]:
             print(1)
             break

#다른사람 풀이
# n, q = map(int, input().split())
# a = []
# b = []
#
# for i in range(1, n + 1):
#     m = int(input())
#     for j in range(m):
#         a.append(i)
#
# for k in range(q):
#     l = int(input())
#     print(a[l])
