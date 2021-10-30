# 2진수를 직접 생성해서 풀어 보았다. 원래는 int함수 하나로 해결되는 문제

x = int(input())
binary = []

while x > 1:
    binary.append(x % 2)
    x //= 2

binary.append(x)
print(binary.count(1))
