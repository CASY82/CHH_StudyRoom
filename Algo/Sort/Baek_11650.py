import sys
n = int(sys.stdin.readline())
loc = []

for _ in range(n):
    loc.append(list(map(int, sys.stdin.readline().split())))

loc.sort(key = lambda x : (x[0], x[1]))

for i,j in loc:
    print(i,j)

# 좀 특이하게 푼 예시가 있어 가져와 봤다. 내 풀이보다 200ms빠르다.
# import sys
#
# lst = sys.stdin.readlines()[1:]
# lst.sort(key=lambda x: int(x.split()[1]))
# lst.sort(key=lambda x: int(x.split()[0]))
# print(''.join(lst))
