# x, y = map(str, input().split())
#
#
# print(int(x[::-1]))
# print(int(y[::-1]))
#
#
# result = str(int(x[::-1]) + int(y[::-1]))[::-1]
#
#
#
# print(result)

#위에거랑 똑같은거 아닌가.. 왜 위는 틀리고 아래는 맞는지 의문이다.
x, y = map(int, input().split())

def rev(num):
    sum = 0
    len_find = len(str(num))

    for i in range(len_find-1, -1, -1):
        sum += (num % 10) * (10 ** i)
        num //= 10

    return sum

print(rev((rev(x) + rev(y))))

