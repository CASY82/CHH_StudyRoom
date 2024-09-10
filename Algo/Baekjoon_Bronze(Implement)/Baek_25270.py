import sys

num = int(sys.stdin.readline())

if num <= 99:
    print(99)
else:
    last_two = num % 100
    lower_bound = num - last_two - 1
    upper_bound = lower_bound + 100

    diff_lower = abs(num - lower_bound)
    diff_upper = abs(num - upper_bound)

    if diff_lower >= diff_upper:
        print(upper_bound)
    else:
        print(lower_bound)

# 다른 사람 풀이1
# original=int(input())
# originalup=original
# originaldown=original
# while True:
#     originalup+=1
#     if originaldown>0:
#         originaldown-=1
#     if "99" in (str(originalup%100)):
#         print(originalup)
#         break
#     elif "99" in (str(originaldown%100)):
#         print(originaldown)
#         break

# 다른 사람 풀이2
# import sys
# input = sys.stdin.readline
#
# n=int(input())
# a=n%100
# if a>=49:
#     print(n//100*100+99)
# elif n<100:
#     print(99)
# else:
#     print(n//100*100-1)