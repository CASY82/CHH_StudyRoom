import sys

t = int(sys.stdin.readline())

for _ in range(t):
    compare, word = sys.stdin.readline().strip().split()

    tmp = compare.count(word)

    print(len(compare) - (len(word) * tmp) + tmp)

# 다른 풀이(나랑 비슷한거 같은데)
# t = int(input())
# for _ in range(t):
#     s, p = input().split()
#     if p in s:
#         temp = s.count(p)
#         print(temp + len(s) - temp*len(p))
#     else:
#         print(len(s))