import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

ori_a = a.zfill(100000)
ori_b = b.zfill(100000)

result_a = ''
result_b = ''

a = int(a, 2)
b = int(b, 2)

and_cal = bin(a & b)[2:].zfill(100000)
or_cal = bin(a | b)[2:].zfill(100000)
xor_cal = bin(a ^ b)[2:].zfill(100000)

for i in range(100000):
    if ori_a[i] == '0':
        result_a += '1'
    else:
        result_a += '0'

    if ori_b[i] == '0':
        result_b += '1'
    else:
        result_b += '0'


print(and_cal)
print(or_cal)
print(xor_cal)
print(result_a)
print(result_b)


#이렇게 간단한 방법이....
# a=int(input(),2)
# b=int(input(),2)
#
# mask=2**100000-1
# print(bin(a&b)[2:].zfill(100000))
# print(bin(a|b)[2:].zfill(100000))
# print(bin(a^b)[2:].zfill(100000))
# print(bin(a^mask)[2:].zfill(100000))
# print(bin(b^mask)[2:].zfill(100000))