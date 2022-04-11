import sys

n, m = map(int, sys.stdin.readline().split())
result = 0

location = list(map(int, sys.stdin.readline().split()))

location.sort()

minus = []
plus = []

for i in location:
    if i > 0:
        plus.append(i)
    else:
        minus.append(i)

# 제일 큰값을 앞으로 가져오기 위함
plus.reverse()
distance = []

# 책 갯수 대로 처리
for i in range(len(minus)//m):
    distance.append(abs(minus[m*i]))
# 만약 나누어 떨어지지 않는다면 해당 책만 따로 다녀옴
if len(minus) % m > 0:
    distance.append(abs(minus[(len(minus)//m)*m]))

# 위와 동일
for i in range(len(plus)//m):
    distance.append(plus[m*i])
if len(plus) % m > 0:
    distance.append(plus[(len(plus)//m)*m])

distance.sort()
# 맨 마지막 거리가 제일 기므로 1번만
result = distance.pop()
# 나머지는 왕복
result += 2*sum(distance)
print(result)