#시간 초과
# while True:
#     try:
#         n, k = map(int, input().split())
#     except:
#         break
#
#     count = n
#
#     while n > 0:
#         n -= k
#         n += 1
#         if n > 0:
#             count += 1
#
#     print(count)


# 성공!
while True:
    try:
        n, k = map(int, input().split())
    except:
        break

    count = n
    coupon = n

    while coupon >= k:
        new = coupon // k
        rest = coupon % k
        count += new
        coupon = (new + rest)

    print(count)