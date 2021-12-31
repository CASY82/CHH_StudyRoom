import sys
sys.setrecursionlimit(10 ** 5)

n = int(sys.stdin.readline())
num = list(sys.stdin.readline().split())
op = list(map(int, sys.stdin.readline().split()))
opList = ['+', '-', '*', '/']
susic = []

result = []

# 1. 숫자가 골라진 시점에서 연산자를 하나씩 넣어본다.
# 2. 골라진 연산자를 개수를 줄이고 남은 것들을 한번씩 돌려서 넣는다.
# 3. 연산자가 모두 배정되었을 때, 수식의 최대 및 최소값을 구한다.

def backtrack(v, susic):
    if v == n-1:
        susic.append(num[v])
        result.append(calc(susic))

    else:
        susic.append(num[v])
        for j in range(len(opList)):
            if op[j] == 0:
                continue
            else:
                op[j] -= 1
                susic.append(opList[j])
                backtrack(v+1, susic)
                op[j] += 1
                susic.pop()
                susic.pop()

def calc(susic):
    tmp = []
    for i in range(len(susic)):
        tmp.append(susic[i])

        if len(tmp) == 3:
            tmp.insert(0, str(int(eval(''.join(tmp)))))
            tmp.pop()
            tmp.pop()
            tmp.pop()

    return int(tmp[0])

backtrack(0, susic)
print(max(result))
print(min(result))

#아니.. 그냥 단순하게 해도 되네..?
# def calcMaxMin(i, sum):
#     if i == n - 1:
#         result.append(sum)
#         return
#
#     if '+' in operator:
#         operator.remove('+')
#         calcMaxMin(i + 1, sum + A[i + 1])
#         operator.append('+')
#     if '-' in operator:
#         operator.remove('-')
#         calcMaxMin(i + 1, sum - A[i + 1])
#         operator.append('-')
#     if '*' in operator:
#         operator.remove('*')
#         calcMaxMin(i + 1, sum * A[i + 1])
#         operator.append('*')
#     if '/' in operator:
#         operator.remove('/')
#         calcMaxMin(i + 1, int(sum / A[i + 1]))
#         operator.append('/')
#
#
# n = int(input())
# A = list(map(int, input().split()))
# l = list(map(int, input().split()))
# operator = ''
# operator += '+' * l[0]
# operator += '-' * l[1]
# operator += '*' * l[2]
# operator += '/' * l[3]
# operator = list(operator)
# result = []
#
# calcMaxMin(0, A[0])
# print(max(result))
# print(min(result))