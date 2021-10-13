dice = list(map(int, input().split()))

if len(set(dice)) == 3:
    print(max(dice) * 100)
elif len(set(dice)) == 2:
    for i in range(1, 7): #이 부분은 리스트를 sort하여 가운데 숫자를 넣어서 해결하면 for를 쓰지 않아도 된다. 정렬하면 가운데 있는 숫자는 무조건 같을테니
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