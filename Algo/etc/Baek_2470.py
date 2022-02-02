# import sys
#
# n = int(sys.stdin.readline())
# solution = list(map(int, sys.stdin.readline().split()))
#
# solution.sort()
#
# start = 0
# end = n-1
# check = 0
#
# while start <= end:
#     mid = (start + end) // 2
#     res = 2000000001
#
#     for i in range(mid):
#         if res > abs(solution[i] + solution[mid]):
#             resultS = i
#             resultE = mid
#             res = abs(solution[resultE] + solution[resultS])
#         else:
#             break
#
#     if res > check:
#         start = mid + 1
#     else:
#         end = mid - 1
#
#     check = res
#
# print(solution[resultS], solution[resultE])

#사실상 투포인터 문제였다고 봐도 될거같다. 이분탐색과 비슷한 방식으로 탐색을 할 뿐인...
import sys

n = int(sys.stdin.readline())
solution = list(map(int, sys.stdin.readline().split()))

solution.sort()

start = 0
end = n - 1
check = 2000000001

while start != end:
    res = solution[start] + solution[end]

    if abs(res) < check:
        resultS = start
        resultE = end
        check = abs(res)

    if res > 0:
        end -= 1
    else:
        start += 1

print(solution[resultS], solution[resultE])