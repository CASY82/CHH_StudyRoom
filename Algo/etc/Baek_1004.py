import math

t = int(input())

def two_point_len(x1, y1, x2, y2):
    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

for i in range(t):
    planet = []
    count = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    for j in range(n):
        planet.append(list(map(int, input().split())))

    for k in range(len(planet)):
        if two_point_len(x1, y1, planet[k][0], planet[k][1]) < planet[k][2] and two_point_len(x2, y2, planet[k][0], planet[k][1]) < planet[k][2]:
            continue

        if two_point_len(x1, y1, planet[k][0], planet[k][1]) < planet[k][2]:
            count += 1

        if two_point_len(x2, y2, planet[k][0], planet[k][1]) < planet[k][2]:
            count += 1

    print(count)


#다른 사람 풀이
# T=int(input())
# for _ in range(T):
#     x1,y1,x2,y2=map(int,input().split())
#     n=int(input())
#     count=0
#     for i in range(n):
#         cx,cy,r=map(int,input().split())
#         loc1=(cx-x1)**2+(cy-y1)**2>r**2
#         loc2=(cx-x2)**2+(cy-y2)**2>r**2
#         if loc1 != loc2:
#             count+=1
#     print(count)