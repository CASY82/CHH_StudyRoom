count = int(input())
divisor = list(map(int, input().split()))

divisor.sort()

if count == 1:
    print(divisor[0] * divisor[0])
else:
    print(divisor[0]*divisor[count-1])

#요 풀이도 괜찮다고 생각이 든다.
# import sys
#
# n = int(sys.stdin.readline())
# a = list(map(int,input().split()))
# print(min(a) * max(a))