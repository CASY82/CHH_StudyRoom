origin_n = int(input())
n = str(origin_n).rjust(2, '0')
num = list(n)
count = 0


while True:
    new_num = ''

    num_result = int(num[0]) + int(num[1])
    new_num += num[1] + str(num_result % 10)

    count += 1

    if origin_n == int(new_num):
        break

    num = list(new_num)

print(count)

#지금보니 리스트로 받을 필요 없이 몫과 나머지로만 사용해서 구할 수 있었다.
#
# num = int(input())
# check = num
# new_num = 0
# temp = 0
# count = 0
# while True:
#     temp = num//10 + num%10
#     new_num = (num%10)*10 + temp%10
#     count += 1
#     num = new_num
#     if new_num == check:
#         break
# print(count)