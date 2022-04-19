import sys

n = int(sys.stdin.readline())
fir_round = list(map(int, sys.stdin.readline().split()))
sec_round = list(map(int, sys.stdin.readline().split()))

result = 0

for i in fir_round:
    if i < 0:
        result += -i
    else:
        result += i

for j in sec_round:
    if j < 0:
        result += -j
    else:
        result += j

print(result)