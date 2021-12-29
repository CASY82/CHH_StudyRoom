import sys

t = int(sys.stdin.readline())

mem = [0, 1] + [0] * 1000000

for _ in range(t):
    case, m = map(int, sys.stdin.readline().split())

    result = [1]

    i = 2
    while True:
        if len(result)>3:
            if result[-1] == 1 and result[-2] == 1:
                result.pop()
                result.pop()
                break

        #이부분만 아이디어를 좀 얻어서 풀었다.
        mem[i] = (mem[i-1] + mem[i-2]) % m
        result.append(mem[i])
        i += 1

    print(case, len(result))