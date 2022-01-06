import sys
sys.setrecursionlimit(10 ** 5)

n = int(sys.stdin.readline())
numList = [str(i) for i in range(9, -1, -1)]

locate = []
tmp = []

#맞게 구현은 했는데 거꾸로 됨;;
def backtrack(startlen, endlen, num):
    if startlen == endlen:
        for i in range(len(locate)):
            if not int(''.join(locate)) in tmp:
                tmp.append(int(''.join(locate)))

    else:
        #집어 넣을 숫자
        for j in range(num, len(numList)):
            locate.append(numList[j])
            backtrack(startlen+1, endlen, j+1)
            locate.pop()

# 9876543210이 마지막 숫자다!
for i in range(11):
    backtrack(0, i, 0)

tmp.sort()

if n < len(tmp):
    print(tmp[n])
else:
    print(-1)

#참고
# from itertools import combinations
#
# n = int(input())
# cnt = 0
# ans = []
#
# # 0 ~ 9로 만들 수 있는 1 ~ 10자리 숫자를 모두 만든 다음 내림차순으로 정렬해서 ans에 저장
# # 마지막에 ans를 다시 오름차순으로 정렬
# for i in range(1, 11):
#     for comb in combinations(range(10), i):
#         res = sorted(comb, reverse=True)
#         ans.append(int(''.join(map(str, res))))
# ans.sort()
#
# try:
#     print(ans[n])
# except:
#     print(-1)