# 메모리 초과
# import sys
# from collections import Counter
#
# n = int(sys.stdin.readline())
# numbers = list(map(int, sys.stdin.readline().split()))
#
# counter = Counter(numbers)
# duplicates = [num for num, count in counter.items() if count > 1]
#
# print(duplicates[0])

import sys

n = int(sys.stdin.readline())
numbers = sys.stdin.read()
n_sum = n * (n-1) // 2

sum_nums = 0
temp = ""
for num in numbers:
    if num.isdigit():
        temp += num
    elif num == " ":
        sum_nums += int(temp)
        temp = ""

sum_nums += int(temp)

print(sum_nums - n_sum)

# 참고 풀이

# import sys
#
#
# def get_range_sum(final_number):
#     return final_number * (final_number - 1) // 2
#
#
# def duplicate_number(N, numbers):
#     sum_numbers = 0
#     temp = ""
#     for num in numbers:
#         if num.isdigit():
#             temp += num
#         elif num == " ":
#             sum_numbers += int(temp)
#             temp = ""
#
#     sum_numbers += int(temp)
#
#     return sum_numbers - get_range_sum(N)
#
#
# if __name__ == "__main__":
#     N = int(input())
#     numbers = sys.stdin.read()
#     print(duplicate_number(N, numbers))