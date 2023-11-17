import sys

n = int(sys.stdin.readline())

if n < 206:
    print(1)
elif n < 218:
    print(2)
elif n < 229:
    print(3)
else:
    print(4)

# import sys
#
# def test(n):
#     if n < 206:
#         print(1)
#     elif n < 218:
#         print(2)
#     elif n < 229:
#         print(3)
#     else:
#         print(4)
#
# for i in range(200, 240):
#     print(i, end=" : ")
#     test(i)