# c, k = map(int, input().split())

# if len(str(c)) > k:
#     print(round(c, -k))
# elif len(str(c)) == k:
#     loca = (10 ** (len(str(c)) - 1))
#     check = c // loca
#
#     if check >= 5:
#         c += (10 - check) * loca
#         print(c)
#     else:
#         print(0)
# else:
#     print(0)

c, k = map(int, input().split())
if k == 0:
    print(c)
else:
    t = 10 ** k
    n = c // t * t
    a = len(str(c)) - k
    if int(str(c)[a]) < 5:
        print(n)
    else:
        print(n + t)
