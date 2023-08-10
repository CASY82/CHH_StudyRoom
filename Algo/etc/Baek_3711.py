import sys

n = int(sys.stdin.readline())

for _ in range(n):
    g = int(sys.stdin.readline())
    student = []
    i = 1

    for _ in range(g):
        student.append(int(sys.stdin.readline()))

    if len(student) == 1:
        print(1)
    else:
        while True:
            tmp = set()
            for stu in student:
                if stu % i not in tmp:
                    tmp.add(stu % i)

            if len(tmp) == len(student):
                print(i)
                break

            i += 1

# 다른 사람 풀이
# import sys
#
# input = sys.stdin.readline
#
#
# def solution(G, student_numbers):
#     m = 1
#     while True:
#         remainder_set = set()
#         for i in student_numbers:
#             remainder = i % m
#             if remainder in remainder_set:
#                 break
#             remainder_set.add(remainder)
#         else:
#             return m
#         m += 1
#
#
# N = int(input())
# for i in range(N):
#     G = int(input())
#     student_numbers = []
#     for j in range(G):
#         nums = int(input())
#         student_numbers.append(nums)
#
#     res = solution(G, student_numbers)
#     print(res)