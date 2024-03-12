import sys

start = list(sys.stdin.readline().strip().split(" : "))
end = list(sys.stdin.readline().strip().split(" : "))

result = 0

for i in range(3):
    start[i] = int(start[i])

for i in range(3):
    end[i] = int(end[i])

if end[2] < start[2]:
    if end[1] <= 0:
        if end[0] <= 0:
            end[0] += 24

        end[0] -= 1
        end[1] += 60

    end[1] -= 1
    end[2] += 60

result += end[2] - start[2]

if end[1] < start[1]:
    if end[0] <= 0:
        end[0] += 24

    end[0] -= 1
    end[1] += 60
result += (end[1] - start[1]) * 60

if end[0] < start[0]:
    end[0] += 24

result += (end[0] - start[0]) * 3600

print(result)

# 다른 사람 풀이
# 아니 이렇게 간단히 하면 되는걸;;
#
# h,m,s=map(int,input().split(" : "))
# a,b,c=map(int,input().split(" : "))
# t=(a*3600+b*60+c)-(h*3600+m*60+s)
# print(t if t>0 else 3600*24+t)