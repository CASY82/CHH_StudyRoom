dice = list(map(int, input().split()))

if len(set(dice)) == 3:
    print(max(dice) * 100)
elif len(set(dice)) == 2:
    for i in range(1, 7):
        if dice.count(i) == 2:
            tmp = i

    print(1000 + (tmp * 100))
else:
    print(max(dice) * 1000 + 10000)

# 다른 사람 풀이
# import sys
# a,b,c = map(int, sys.stdin.readline().split())
# if a==b==c:
#     print(10000+(a*1000))
# elif a == b or a == c :
#     print(1000 + (a*100))
# elif b == c:
#     print(1000 + (b*100))
# else:
#     print(max(a,b,c)*100)