import sys

n = int(sys.stdin.readline())
product = []
result = 0

for _ in range(n):
    product.append(int(sys.stdin.readline()))

product.sort()

while product:
    if len(product) >= 3:
        a = product.pop()
        b = product.pop()
        product.pop()

        result += a + b
    else:
        result += product.pop()

print(result)