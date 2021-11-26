# 도저히 반례를 모르겠다....
# c, k = map(int, input().split())
#
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

#현재 제출한 코드... 인터넷에서 긁어온 소스이다. 순수하게 값을 구하는 형태
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

# 내 코드와 가장 비슷하다고 보는데, 내가 해결하지 못한 반례가 해결된 모습인거 같다.
# a, b = map(int, input().split())
# if len(str(a)) >= b+1:
#     print(round(a, -b))
# else:
#     if 5*10**(b-1) <= a: print(10**b)
#     else: print(0)