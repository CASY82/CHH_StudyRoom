import sys

n = int(sys.stdin.readline())
slime = list(map(int, sys.stdin.readline().split()))
result = 0

slime.sort(reverse=True)

while len(slime) > 1:
    a = slime.pop()
    b = slime.pop()

    result += (a*b)

    slime.append(a+b)

print(result)