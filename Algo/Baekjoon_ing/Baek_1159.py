n = int(input())
player = []
name = []
result = ''

for i in range(n):
    player.append(input())

for i in range(len(player)):
    name.append(player[i][0])

name_list = list(set(name))
count = [0 for i in range(len(name_list))]

for i in name_list:
    for j in name:
        if i == j:
            count[name_list.index(i)] += 1

for i in range(len(count)):
    if count[i] >= 5:
        result += name_list[i]

if result == '':
    result = 'PREDAJA'
else:
    result_list = list(result)
    result = ''.join(sorted(result_list))

print(result)

#다른 사람의 풀이

# from collections import Counter
# n = int(input())
# player = []
# fn = []
# cnt = 0
# for i in range(n):
#     a = input()
#     player.append(a[0])   #앞글자만 받아오는 방법
# player_count = Counter(player)
# for i, j in player_count.items():  #딕셔너리 형태로 만들어준다는 사실을 기억할 것
#     if j >= 5:
#         fn.append(i) #딕셔너리의 첫 번째 원소만 넣는 방법
#         cnt += 1
# fn.sort()
# if cnt == 0:
#     print("PREDAJA")
# else:
#     for i in fn:
#         print(i, end='')

