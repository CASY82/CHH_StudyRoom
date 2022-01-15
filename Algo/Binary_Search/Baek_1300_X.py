# import sys

#일단 시간 복잡도 생각 안하고 구현(시간 복잡도 이전에 IDE에서도 메모리 오류 뜨네...)

# n = int(sys.stdin.readline())
# a = []
# 
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         a.append(i*j)
# 
# a.sort()
# print(a)

# 아무리 생각해도 아래 식은 시간초과가 날것 같다.
# def check(n, m):
#     cnt = 0
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if i*j < m:
#                 cnt += 1
#             else:
#                 break
#
#     return cnt

# 이분탐색을 구현하는건 문제가 안되었는데, 이분탐색을 이용해서 중간에 수를 더하는 과정 자체를 생각했어야 하는 문제여서 못풀었다.
# 애초에 어떤식으로 접근해야하는지 감조차 잡히지 않았음...
# 다른사람 풀이 참고하여 넘어감
import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

start = 1
end = n*n


while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for i in range(1, n+1):
        cnt += min((mid // i), n)

    if cnt >= k:
        end = mid - 1
    else:
        start = mid + 1

print(start)