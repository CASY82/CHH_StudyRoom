import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

right = 0
right_result = 0
left = 0
left_result = 0

for i in range(len(array)):
    if array[i] % 2 == 0:
        left_result += left
    else:
        left += 1

for j in range(len(array) - 1, -1, -1):
    if array[j] % 2 == 0:
        right_result += right
    else:
        right += 1

print(min(right_result, left_result))

# 다른 사람 풀이
# n=int(input())
# arr=list(map(int,input().split()))
# even=0
# ec=0
# odd=0
# oc=0
# for ind,a in enumerate(arr):
#     if a%2==0:
#         even+=ind-ec
#         ec+=1
#     else:
#         odd+=ind-oc
#         oc+=1
# print(min(even,odd))