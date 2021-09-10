# 일단 못품. 정답을 보니 정말 간단한 문제였다...

# N = int(input())
# tmp = []
#
#
# while True:
#     if N % 10 == 7 or N % 10 == 4:
#         tmp.append(str(N % 10))
#     else:
#         tmp.append('7')
#
#     N = N // 10
#
#     if N < 4:
#         break
#
# print(int(''.join(tmp)))

#주어진 수를 줄여가며 일일히 비교하는 방법을 사용한 코드, 왜 못풀었을까...? 그냥 수를 하나씩 일일히 증가시켜서 비교해보면 되는걸...

n = int(input())
while True:
    flag = True
    for i in str(n):
        if i!="4" and i!="7":
            flag = False
            n -= 1
    if flag :
        print(n)
        break