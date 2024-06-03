import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()
s3 = sys.stdin.readline().strip()

check1 = False
check2 = False
check3 = False

if "l" in (s1[0], s2[0], s3[0]):
    check1 = True

if "k" in (s1[0], s2[0], s3[0]):
    check2 = True

if "p" in (s1[0], s2[0], s3[0]):
    check3 = True

if check1 and check2 and check3:
    print("GLOBAL")
else:
    print("PONIX")

# 다른 사람 풀이
# a = []
# for i in range(3):a.append(input())
# a.sort()
# print(['PONIX', 'GLOBAL'][a[0][0] == 'k' and a[1][0] == 'l' and a[2][0] == 'p'])