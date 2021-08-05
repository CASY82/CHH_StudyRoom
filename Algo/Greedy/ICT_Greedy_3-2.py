#큰 수의 법칙

n, m, k = map(int, input().split())

array = list(map(int, input().split()))
result = 0
count = 0



array.sort(reverse=True)


for i in range(m):
    if k != count:
        result += array[0]
        count += 1
    else:
        result += array[1]
        count = 0

print(result)


#답안 예시

# n, m, k = map(int, input().split())
#
# data = list(map(int, input().split()))
#
# data.sort()
# first = data[n - 1]
# second = data[n - 2]
#
# result = 0
#
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#
#         result += first
#         m -= 1
#
#     if m == 0:
#         break
#
#     result += second
#     m -= 1
#
# print(result)

#수열을 이용한 답안

# n, m, k = map(int, input().split())
#
# data = list(map(int, input().split()))
#
# data.sort()
# first = data[n - 1]
# second = data[n - 2]
#
# count = int(m / (k + 1)) * k
# count += m % (k + 1)
#
# result = 0
# result += (count) * first
# result += (m - count) * second
#
# print (result)