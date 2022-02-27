# import sys
#
# n = int(sys.stdin.readline())
# bulb = list(sys.stdin.readline().strip())
# bulb2 = bulb[:]
# result = list(sys.stdin.readline().strip())
# cnt = 0
# cnt2 = 0
#
# # 0 번을 누른 경우
# for j in range(2):
#     if bulb[j] == '0':
#         bulb[j] = '1'
#     else:
#         bulb[j] = '0'
# cnt += 1
#
# for i in range(1, len(bulb)):
#     if i == len(bulb)-1:
#         if bulb[i - 1] != result[i - 1]:
#             for j in range(i-1, i+1):
#                 if bulb[j] == '0':
#                     bulb[j] = '1'
#                 else:
#                     bulb[j] = '0'
#
#             cnt += 1
#     else:
#         if bulb[i + 1] != result[i + 1] or bulb[i - 1] != result[i - 1]:
#             for j in range(i-1, i+2):
#                 if bulb[j] == '0':
#                     bulb[j] = '1'
#                 else:
#                     bulb[j] = '0'
#             cnt += 1
#
# # 0 번을 누르지 않은 경우
# for i in range(1, len(bulb2)):
#     if i == len(bulb2)-1:
#         if bulb2[i - 1] != result[i - 1]:
#             for j in range(i-1, i+1):
#                 if bulb2[j] == '0':
#                     bulb2[j] = '1'
#                 else:
#                     bulb2[j] = '0'
#
#             cnt2 += 1
#     else:
#         if bulb2[i + 1] != result[i + 1] or bulb2[i - 1] != result[i - 1]:
#             for j in range(i-1, i+2):
#                 if bulb2[j] == '0':
#                     bulb2[j] = '1'
#                 else:
#                     bulb2[j] = '0'
#             cnt2 += 1
#
# if result == bulb2:
#     print(cnt2)
# elif result == bulb:
#     print(cnt)
# else:
#     print(-1)

#결국 다른 사람 코드 참고하여 풀이 위 코드 왜자꾸 틀리는지 모르겠다...
import sys

def zeroClick(state):
    count=1
    state[0] = int(not state[0])
    state[1] = int(not state[1])
    for i in range(1,n):
        if(state[i-1]!=result[i-1]):
            #카운트 위치 차이인가...
            count+=1
            state[i-1]=int(not state[i-1])
            state[i]=int(not state[i])
            if(i!=n-1):
                state[i+1]=int(not state[i+1])
    if(state==result):
        return count
    else:
        return -1
def zeroNoClick(state):
    count = 0
    for i in range(1,n):
        if(state[i-1]!=result[i-1]):
            # 카운트 위치 차이인가...
            count+=1
            state[i-1]=int(not state[i-1])
            state[i]=int(not state[i])
            if(i!=n-1):
                state[i+1]=int(not state[i+1])
    if(state==result):
        return count
    else:
        return -1

n = int(sys.stdin.readline().strip())
state = list(map(int, sys.stdin.readline().strip()))
result = list(map(int, sys.stdin.readline().strip()))
result1 = zeroClick(state[:])
result2 = zeroNoClick(state[:])
if(result1>=0 and result2>=0):
    print(min(result1, result2))
elif(result1 >= 0 and result2 < 0):
    print(result1)
elif(result1 < 0 and result2 >= 0):
    print(result2)
else:
    print(-1)