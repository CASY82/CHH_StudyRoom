import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
c = sys.stdin.readline().strip()

array = [a, b, c]
now_idx = 0
now_num = 0

for i in range(len(array)):
    if array[i] not in ["Fizz", "Buzz", "FizzBuzz"]:
        now_num = int(array[i])
        now_idx = i + 1

for j in range(4 - now_idx):
    now_num += 1

if now_num % 3 == 0 and now_num % 5 == 0:
    print("FizzBuzz")
elif now_num % 3 == 0:
    print("Fizz")
elif now_num % 5 == 0:
    print("Buzz")
else:
    print(now_num)

# 다른 사람 풀이
# import sys
#
# for i in range(3):
#     data = sys.stdin.readline().strip()
#     if data.isdigit():
#         answer = int(data) + (3 - i)
#         break
#
# result = ''
# if answer % 3 == 0:
#     result += 'Fizz'
# if answer % 5 == 0:
#     result += 'Buzz'
#
# if not result:
#     result = answer
#
# print(result)
