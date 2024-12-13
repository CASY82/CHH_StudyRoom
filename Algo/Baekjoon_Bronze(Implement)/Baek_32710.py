import sys

n = int(sys.stdin.readline())

gugudan_result = set()

for i in range(1, 10):
    for j in range(1, 10):
        gugudan_result.add(i * j)

if n in gugudan_result:
    print(1)
else:
    print(0)