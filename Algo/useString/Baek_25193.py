import sys

n = int(sys.stdin.readline())
sickdan = sys.stdin.readline().strip()

length = len(sickdan)
chicken = sickdan.count("C")

tmp = length - chicken + 1

print(length // tmp)

# 다른 사람 풀이(비슷하다)

# import math
# import sys
#
# days = int(sys.stdin.readline().strip())
# my_husband_meal = sys.stdin.readline().strip()
# cnt_c = my_husband_meal.count('C')
# cnt_others = days-cnt_c
#
# print( int(math.ceil(cnt_c / (cnt_others + 1) )) )