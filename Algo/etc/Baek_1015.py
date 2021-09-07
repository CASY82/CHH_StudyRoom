#문제 이해가 안되서 문제 이해만 도움을 받고 로직 및 구현은 직접하였다.

n = int(input())
a = list(map(int, input().split()))

def sort_map(array):
    index_arr = []
    result = []

    for i in enumerate(array):
        index_arr.append(list(i))

    index_arr.sort(key = lambda x : x[1])

    for j in range(len(array)):
        result.append(index_arr[j][0])

    return result

b = sort_map(a)
result = sort_map(b)

for i in result:
    print(i, end=' ')

#다른사람 풀이 deque를 써서 풀었네...
# import sys
# input = sys.stdin.readline
# from collections import defaultdict, deque
#
# N = int(input())
# A = list(map(int, input().split()))
#
# arr = defaultdict(deque)
# B = sorted(A)
#
# for i in range(len(B)):
#     arr[B[i]].append(i)
#
# for i in range(len(A)):
#     print(arr[A[i]].popleft(), end=" ")
