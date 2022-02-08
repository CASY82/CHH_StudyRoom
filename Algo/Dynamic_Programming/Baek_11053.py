#직접짠 로직 성공!
import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

newNumArr = [0]

for i in num:
    if newNumArr[-1] < i:
        newNumArr.append(i)
    else:
        for j in range(1, len(newNumArr)):
            if newNumArr[j] >= i:
                newNumArr[j] = i
                break

print(len(newNumArr)-1)

#전통적인 방법(dp) 로직(java)
# for (int k = 0; k < n; k++){
# 	length[k] = 1;
#     for (int i = 0; i < k; i++){
#         if(arr[i] < arr[k]){
#             length[k] = max(length[k], length[i] + 1);
#         }
#     }
# }

# import sys
# input = sys.stdin.readline
#
# n = int(input())
# a = list(map(int, input().split()))
#
# dp = [0 for i in range(n)]
#
# for i in range(n):
#     for j in range(i):
#         if a[i] > a[j] and dp[i] < dp[j]:
#             dp[i] = dp[j]
#     dp[i] += 1
#
# print (max(dp))