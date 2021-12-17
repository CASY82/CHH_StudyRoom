import sys

word = sys.stdin.readline().strip()

zero = [x for x in word.split("0") if x]
one = [x for x in word.split("1") if x]

print(min(len(zero), len(one)))

#와... 01, 10이 바뀌는부분을 세는 방법;;;
# v=input().count
# print((v('10')+v('01')+1)//2)