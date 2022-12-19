import sys
sys.setrecursionlimit(30000)

a, b, c = map(int, sys.stdin.readline().split())

def divide(num ,zegop, namuji):
    if zegop == 1:
        return num % namuji
    else:
        tmp = divide(num, zegop // 2, namuji)
        if zegop % 2 == 0:
            return tmp * tmp % namuji
        else:
            return tmp * tmp * num % namuji

print(divide(a, b, c))