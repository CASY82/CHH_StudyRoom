# 숫자 찾기

# def solution(num, total):
#     tmp = total
#
#     while tmp >= -9000:
#         answer = []
#
#         for i in range(tmp, tmp - num, -1):
#             answer.append(i)
#
#         tmp -= 1
#
#         if sum(answer) == total:
#             break
#
#     return answer[::-1]

def solution(num, total):
    start = (total - (num * (num - 1) // 2)) // num
    return [i for i in range(start, start + num)]

print(solution(3, 12))
print(solution(5, 15))
print(solution(4, 14))
print(solution(5, 5))

print(solution(1, 1000))