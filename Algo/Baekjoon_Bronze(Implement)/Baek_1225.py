#pypy3로 해서 맞음
import time
start = time.time()
A, B = input().split()

result = 0

for i in range(len(A)):
    for j in range(len(B)):
        result += (int(A[i]) * int(B[j]))

print(result)
print("time : ", time.time() - start)


#python 풀이

# import time
# start = time.time()
# a,b = input().split()
# a = list(map(int,a))
# b = list(map(int,b))
# b = sum(b) #두 수를 더한거 곱한것과 같다
# total = 0
#
# for i in a:
#     total += b*i
# print(total)
# print("time : ", time.time() - start)
