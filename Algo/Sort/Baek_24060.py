# 불필요하게 도는 재귀가 있거나, while문이 있는거 같음 이 부분 해결 필요
import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
counter = [0]

def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)

def finish(num):
    print(num)
    exit()

def merge(arr, start, mid, end):
    i = start
    j = mid + 1
    t = 0

    tmp = [0] * (end - start + 1)

    while i <= mid and j <= end:
        counter[0] += 1
        if arr[i] <= arr[j]:
            tmp[t] = arr[i]
            i += 1
        else:
            tmp[t] = arr[j]
            j += 1

        if counter[0] == k:
            finish(tmp[t])

        t += 1

    while i <= mid:
        tmp[t] = arr[i]
        counter[0] += 1
        if counter[0] == k:
            finish(tmp[t])
        t += 1
        i += 1

    while j <= end:
        tmp[t] = arr[j]
        counter[0] += 1
        if counter[0] == k:
            finish(tmp[t])
        t += 1
        j += 1

    # 없어도 되는 줄 알았는데.. 알고보니 제일 중요한 부분이다 왜 없어도 된다고 생각했을까..?
    i = start
    t = 0

    while i <= end:
        arr[i] = tmp[t]
        t += 1
        i += 1

merge_sort(arr, 0, n-1)
print(-1)

# 얜 순서가 틀림. 제시해준 수도코드랑 로직이 다르기 때문에 중간에 푸는 과정 중 답이 필요한 경우인지라...
# import sys
#
# n, k = map(int, sys.stdin.readline().split())
# arr = list(map(int, sys.stdin.readline().split()))
# counter = [0]
#
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]
#
#     left_ = merge_sort(left)
#     right_ = merge_sort(right)
#     return merge(left_, right_)
#
# def merge(left, right):
#     i, j = 0, 0
#     tmp = []
#
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             tmp.append(left[i])
#             counter[0] += 1
#             if counter[0] == k:
#                 print(left[i])
#                 exit()
#             i += 1
#
#         else:
#             tmp.append(right[j])
#             counter[0] += 1
#             if counter[0] == k:
#                 print(right[j])
#                 exit()
#
#             j += 1
#
#     while i < len(left):
#         tmp.append(left[i])
#         counter[0] += 1
#         if counter[0] == k:
#             print(left[i])
#             exit()
#
#         i += 1
#
#     while j < len(right):
#         tmp.append(right[j])
#         counter[0] += 1
#         if counter[0] == k:
#             print(right[j])
#             exit()
#
#         j += 1
#
#     return tmp
#
# merge_sort(arr)
# print(-1)

# 통과하는 소스 왜 통과할까?
# import sys
# input = sys.stdin.readline
# n, k = list(map(int, input().split()))
# _v = list(map(int,input().split()))
# ans = -1
#
# def merge_sort(v, i, j):
#     if i < j:
#         m = (i+j)//2
#         merge_sort(v, i, m)
#         merge_sort(v, m+1, j)
#         merge(v, i, m+1, j)
#
# def merge(v, i, m, j):
#     global k
#     global ans
#     p = i
#     q = m
#     r = 0
#     temp = [0] * (j-i+1)
#     while p < m and q <= j:
#         k-=1
#         if v[p] > v[q]:
#             temp[r] = v[q]
#             q+=1
#         else:
#             temp[r] = v[p]
#             p+=1
#         if k == 0:
#             ans = temp[r]
#         r+=1
#
#     while p < m:
#         temp[r] = v[p]
#         k-=1
#         if k == 0:
#             ans = temp[r]
#         p+=1
#         r+=1
#
#     while q <= j:
#         temp[r] = v[q]
#         k-=1
#         if k == 0:
#             ans = temp[r]
#         q+=1
#         r+=1
#
#     p=i
#     i=0
#     while p<=j:
#         v[p] = temp[i]
#         p+=1
#         i+=1
#
# merge_sort(_v, 0, n-1)
# print(ans)