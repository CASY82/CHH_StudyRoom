#결국 못풀었다. 다른사람의 풀이를 참고하여 숙지하도록 하자. 에라토스테네스의 체를 쓴다는 것만 알고 나머지는 제대로 구현을 못한 사례...(계속 시간초과로 인해 못품)

p, k = map(int, input().split())

prime = [False, False] + [True] * (k-2)
for i in range(2, int(k**0.5)+1):
    if prime[i]:
        for j in range(i+i, k, i):
            if prime[j]:
                prime[j] = False


flag = True
for i in range(2, k):
    if prime[i]:
        if p % i == 0:
            flag = False
            break

if flag:
    print('GOOD')
else:
    print('BAD', i)

# 참고용,,, 이건 무슨...

# pw, key = map(int, input().split())
# if pw % 2 == 0 and key > 2:
#     print('BAD', 2)
#     exit()
# elif pw % 3 == 0 and key > 3:
#     print('BAD', 3)
#     exit()
# for i in range(5, key, 2):
#     if pw % i == 0:
#         print('BAD', i)
#         exit()
# print('GOOD')