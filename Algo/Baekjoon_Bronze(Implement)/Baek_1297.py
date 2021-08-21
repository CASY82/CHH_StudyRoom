import math

d, h, w = map(int, input().split())

width = (d * w) / (((w**2)+(h**2))**(1/2))
height = (d * h) / (((w**2)+(h**2))**(1/2))

print(math.trunc(height), math.trunc(width), end=' ')


#다른 사람 풀이
# 변수를 적극적으로 활용하는 것이 좀더 보기 좋아 보인다는 것을 깨달았다.
# import math
#
# D, H, W = map(int, input().split(' '))
#
# C = math.sqrt(H*H + W*W)
#
# per = C/D
#
# print("{0} {1}".format(int(H/per), int(W/per)))