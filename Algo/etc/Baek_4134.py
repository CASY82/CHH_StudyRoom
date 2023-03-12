import sys
import math

t = int(sys.stdin.readline())

def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        #나눠지면 소수가 아님
        if n % i == 0:
            return False

    return True


for _ in range(t):
    num = int(sys.stdin.readline())

    if num == 0 or num == 1:
        print(2)
        continue

    while True:
        if prime(num):
            print(num)
            break

        num += 1