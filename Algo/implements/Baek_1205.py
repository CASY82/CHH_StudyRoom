import sys
n, score, p = map(int, sys.stdin.readline().split())

if n > 0:
    scores = list(map(int, sys.stdin.readline().split()))
    rank = n

    for i in range(len(scores)):
        if scores[len(scores) - 1 - i] >= score:
            result = rank
            break

        rank -= 1

    if scores[-1] >= score and n >= p:
        rank = -1
    else:
        rank -= scores.count(score) - 1
else:
    rank = 1

print(rank)

#좀더 깔끔하게 된 코드 참고

# a,b,c= map(int,input().split())
# d=[]
# if a:
#     d=list(map(int,input().split()))
# while(len(d)!=c):
#     d.append(-1)
# for i in range(len(d)):
#     if d[i]<=b:
#         break
#     i=-2
# if b==d[-1]:
#     i=-2
# print(i+1)