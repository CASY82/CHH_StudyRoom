import sys
n, k = map(int, sys.stdin.readline().split())
cats = list(map(int, sys.stdin.readline().split()))

cats.sort()

end = len(cats) - 1
result = 0

for i in range(len(cats)):
    if i != end:
        while i < end:
            if k < cats[i] + cats[end]:
                end -= 1
            else:
                end -= 1
                result += 1
                break
    else:
        break

print(result)

# 다른 사람 풀이

# import sys
# input = sys.stdin.readline
#
# n , k = map(int, input().split())
#
# weights = list(map(int, input().split()))
#
# weights.sort()
#
# it = 0
# rit = n - 1
# max = 0
#
# while it < rit:
#   if weights[it] + weights[rit] <= k:
#     it += 1
#     rit -= 1
#     max += 1
#     continue
#   rit -= 1
#
# print(max)