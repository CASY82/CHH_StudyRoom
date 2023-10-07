import sys

start = int(sys.stdin.readline())
end = int(sys.stdin.readline())

if 20 <= start <= 24:
    tmp_st = 24 - start

    print(tmp_st + end)
else:
    print(end - start)

# 더 깔끔 풀이

# a,b=map(int,open(0))
# print((b-a+24)%24)