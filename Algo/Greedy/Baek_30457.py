import sys
from collections import Counter


def limit_duplicates(lst):
    # 리스트의 각 요소의 개수를 세기
    counts = Counter(lst)

    # 결과를 저장할 리스트
    result = []

    # 각 요소와 그 개수를 확인
    for num, count in counts.items():
        # 2개 이하인 경우 모두 추가하고, 3개 이상인 경우 2개만 추가
        result.extend([num] * min(count, 2))

    return result

n = int(sys.stdin.readline())
student = list(sys.stdin.readline().split())

def expand_around_max(lst):
    # 리스트에서 최댓값 찾기
    max_value = max(lst)

    # 최댓값의 인덱스 찾기
    max_index = lst.index(max_value)

    # 최댓값을 1개만 남기고 나머지 제거
    result = [max_value]

    # 왼쪽과 오른쪽 요소 추가
    left_part = lst[:max_index]
    right_part = lst[max_index + 1:]

    # 왼쪽 요소 추가
    result.extend(left_part)

    # 오른쪽 요소 추가
    result.extend(right_part)

    return result

new_list = limit_duplicates(student)
expanded_list = expand_around_max(new_list)
print(len(expanded_list))

# 다른 사람 풀이
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
# answer = 0
# remain = []
#
# last = 0
# for i in range(n):
#     if last < arr[i]:
#         answer += 1
#         last = arr[i]
#     else:
#         remain.append(arr[i])
#
# print(answer + len(set(remain)))