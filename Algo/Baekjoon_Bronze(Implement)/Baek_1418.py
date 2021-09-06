n = int(input())
k = int(input())

count = 0

for i in range(1, n+1):
     num = i
     check = 0
     j = 2

     while num != 1:
         if j > k:
             check = 1
             break

         if num % j == 0:
             num //= j
         else:
             j += 1

     if check == 0:
         count += 1


print(count)

# 다른 사람 풀이 참고

# n = int(input())
# k = int(input())
# r = 1
#
# def check(num):
#     pf = 2
#     while num != 1:
#         if pf > k:
#             return False
#         if num%pf == 0:
#             num = num//pf
#         else:
#             pf += 1
#     return True
#
# for i in range(2,n+1):
#     if check(i):
#         r += 1
#
#
# print(r)