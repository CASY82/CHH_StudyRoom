import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

def gcd_of_numbers(numbers):
    gcd_result = numbers[0]
    for i in range(1, len(numbers)):
        gcd_result = gcd(gcd_result, numbers[i])
    return gcd_result

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#여기 알고리즘 개선 필요
def common_divisors(numbers):
    gcd_result = gcd_of_numbers(numbers)
    divisors = []
    for i in range(1, int(gcd_result ** 0.5) + 1):
        if gcd_result % i == 0:
            divisors.append(i)
            if i != gcd_result // i:
                divisors.append(gcd_result // i)
    divisors.sort()
    return divisors

result = common_divisors(numbers)
for num in result:
    print(num)