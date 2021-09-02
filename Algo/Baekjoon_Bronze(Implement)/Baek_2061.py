#1837번이랑 똑같은 문제다;;;

k, l = map(int, input().split())

prime = [False, False] + [True] * (l - 2)

for i in range(2, int(l**0.5) + 1):
    if prime[i]:
        for j in range(i+i, l, i):
            if prime[j]:
                prime[j] = False

flag = True

for i in range(2, l):
    if k % i == 0:
        flag = False
        break

if flag:
    print("GOOD")
else:
    print('BAD', i)

#참고용
# k,l=map(int,input().split())
# t=0
# for i in range(2,l):
#     if k%i==0:
#         print("BAD "+str(i))
#         t=1
#         break
# if t==0:
#     print("GOOD")