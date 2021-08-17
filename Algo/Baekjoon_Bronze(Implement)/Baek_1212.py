# num = str(input())
# num = num[::-1]
# result = 0
#
# for i in range(len(num)):
#     result += int(num[i]) * (8 ** i)
#
# print(format(result, 'b'))

num = int(input(), 8)
print(format(num, 'b'))
