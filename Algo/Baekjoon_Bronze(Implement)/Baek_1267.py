from sys import stdin

n = int(stdin.readline())
call_time = [int(x) for x in input().strip().split()]
result_min = 0
result_young = 0

def youngsik(time):
    fee = (time // 30) + 1
    return fee * 10

def minsik(time):
    fee = (time // 60) + 1
    return fee * 15

for i in call_time:
    result_min += minsik(i)
    result_young += youngsik(i)

if result_young > result_min:
    print('M', result_min)
elif result_young == result_min:
    print('Y M', result_min)
else:
    print('Y', result_young)

#좀더 쉽게 하는 법

# N = int(input())
# time = list(map(int,input().split()))
#
# Y=0
# M=0
# for i in time:
#     Y += (i//30)*10+10
#     M += (i//60)*15+15
#
# if Y<M:
#     print("Y", Y)
# elif Y==M:
#     print("Y","M",Y)
# else:
#     print("M",M)