# 메모리 초과
# from itertools import permutations
#
# n = int(input())
# n_list = [i for i in range(1, n+1)]
# compare_list = list(map(int, input().split()))
# compared_list = []
#
# for i in permutations(n_list, n):
#     compared_list.append(list(i))
#
# result = compared_list.index(compare_list)
#
# if result > 0:
#     print(compared_list[result-1])
# else:
#     print(-1)

#알고리즘 순서
# 1. a[k] > a[k+1]가 성립하는 k의 최댓값 구하기
# 2. k 이후 값들 중 a[k] > a[m]이 성립하는 m 최댓값
# 3. k,m 값 자리 변경
# 4. 인덱스 k 이후 값들을 내림차순 정렬

n = int(input())
compare_list = list(map(int, input().split()))
bigger = 0

if sorted(compare_list) == compare_list:
    print(-1)
else:
    for i in range(len(compare_list) - 1):
        if compare_list[i] > compare_list[i + 1]:
            bigger = i

    for j in range(bigger + 1, len(compare_list)):
        if compare_list[bigger] > compare_list[j]:
            second = j

    compare_list[bigger], compare_list[second] = compare_list[second], compare_list[bigger]

    tmp = compare_list[bigger+1:]
    tmp.sort(reverse=True)
    answer = compare_list[:bigger + 1] + tmp

    for k in answer:
        print(k, end=' ')
