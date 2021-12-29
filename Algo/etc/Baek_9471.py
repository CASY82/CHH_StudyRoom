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

        #이 부분만 아이디어를 좀 얻어서 풀었다.
        mem[i] = (mem[i-1] + mem[i-2]) % m
        result.append(mem[i])
        i += 1

    print(case, len(result))

# 내 코드를 줄이면 최종적으로 이 모양이 되지 않을까 해서 가져온 첨부 코드

# import sys
# input = sys.stdin.readline
#
# p = int(input())
# answer = []
#
# def fibo (num):
#     lst = [1,1]
#     while True:
#         lst.append((lst[-1]+lst[-2])%num)
#         if lst[-1] == 0 and lst[-2] == 1:
#             return len(lst)
#
# for _ in range(p):
#     n,m = map(int,input().split())
#     answer.append(f'{n} {fibo(m)}')
#
# print('\n'.join(answer))