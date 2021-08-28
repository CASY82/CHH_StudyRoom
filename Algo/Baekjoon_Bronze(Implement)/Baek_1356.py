n = list(map(int, input()))
result = False


for i in range(len(n)):
    front = 1
    back = 1

    for j in range(i, len(n)):
        back *= n[j]

    for k in range(0, i):
        front *= n[k]

    if back == front:
        result = True
        break

if len(n) == 1:
    print('NO')
else:
    if result == True:
        print('YES')
    else:
        print('NO')

#다른 사람 풀이
# 내 로직과 다 동일하지만 가져온 이유는 제일 처음 range에 1을 넣어서 1이 들어갔을 때 YES가 나오는 것을 방지한 것 때문에 가져옴
# m = list(map(int, input()))
# l=len(m)
# check=0
# for i in range(1, l):
#     a=1
#     b=1
#     for j in range(0,i):
#         a = a*m[j]
#     for j in range(i,l):
#         b = b*m[j]
#     if a==b:
#         check += 1
#         break
# if (check==1):
#     print('YES')
# else:
#     print('NO')