#그리디에 대해서 깨달을 수 있었다.
import sys

n = int(sys.stdin.readline())
street = list(map(int, sys.stdin.readline().split()))
city = list(map(int, sys.stdin.readline().split()))

result = 0
oil = city[0]
for i in range(len(street)):
    result += oil * street[i]

    if city[i+1] < oil:
        oil = city[i+1]

print(result)