#시간 초과가 계속 나길래... 입력을 받는 걸 앞으로 다음과 같이 해야겠다... (stdin.readline())
from sys import stdin

for _ in range(3):
    n = int(stdin.readline())
    sum = 0

    for _ in range(n):
        sum += int(stdin.readline())

    if sum == 0:
        print('0')
    elif sum > 0:
        print('+')
    else:
        print('-')
