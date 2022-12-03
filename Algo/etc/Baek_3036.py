import sys

n = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))
num_len = len(num)

#유클리드 호제법이 필요하네ㅋㅋ
def GCD(a, b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a%b)

for i in range(1, num_len):
    tmp = GCD(num[0], num[i])

    print("{0}/{1}".format(num[0] // tmp, num[i] // tmp))