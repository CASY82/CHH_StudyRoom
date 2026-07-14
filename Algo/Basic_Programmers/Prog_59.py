# flag에 따라 다른 값 반환하기
import sys

n = int(sys.stdin.readline())

if n % 2 == 0:
    print("{} is even".format(n))
else:
    print("{} is odd".format(n))