import sys

n, m = map(int, sys.stdin.readline().split())

school = []
result = 0

for _ in range(m):
    school.append(int(sys.stdin.readline()))

school.sort()

for i in range(m):
    if n >= school[i]:
        n -= school[i]
        result += 1
    else:
        break

print(result)

# 다른 사람 풀이
# n,k,*l=map(int,open(0).read().split())
# l.sort()
# s=0
# for i,v in enumerate(l):
#     if(s:=s+v)>n:k=i;break
# print(k)