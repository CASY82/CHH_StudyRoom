#한번에 정답
minsik = input()
girls = int(input())
girls_list = []

for _ in range(girls):
    girls_list.append(input())

def love_cal(minsik, girls_list):
    girl_love = []

    girls_list.sort()

    for i in girls_list:
        L = minsik.count('L') + i.count('L')
        O = minsik.count('O') + i.count('O')
        V = minsik.count('V') + i.count('V')
        E = minsik.count('E') + i.count('E')

        girl_love.append(((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100)

    return girls_list[girl_love.index(max(girl_love))]


print(love_cal(minsik, girls_list))

#다른 사람 풀이 참고
#
# ms = input()
# n = int(input())
# li = sorted([input() for i in range(n)])
# max_p = max_i = 0
# for i in range(n):
#     L = ms.count("L") + li[i].count("L")
#     O = ms.count("O") + li[i].count("O")
#     V = ms.count("V") + li[i].count("V")
#     E = ms.count("E") + li[i].count("E")
#     p = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
#     if max_p < p:
#         max_p = p
#         max_i = i
# print(li[max_i])

