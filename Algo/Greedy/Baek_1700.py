import sys

n, k = map(int, sys.stdin.readline().split())
multitap = []

use = list(map(int, sys.stdin.readline().split()))
elecCnt = [0] + [0] * k
cnt = 0

for i in range(k):
    elecCnt[use[i]] += 1

for i in range(len(use)):
    if len(multitap) < n:
        if use[i] not in multitap:
            multitap.append(use[i])
        elecCnt[use[i]] -= 1
    else:
        if use[i] in multitap:
            elecCnt[use[i]] -= 1
            continue

        check = True
        for j in range(n):
            if elecCnt[multitap[j]] == 0:
                multitap[j] = use[i]
                elecCnt[use[i]] -= 1
                cnt += 1
                check = False
                break

        if check:
            tmpArray = use[i + 1:]
            tmpIdx = 0
            tmpElec = 0

            for j in range(n):
                if multitap[j] in tmpArray and tmpArray.index(multitap[j]) >= tmpIdx:
                    tmpIdx = tmpArray.index(multitap[j])
                    tmpElec = multitap[j]

            multitap[multitap.index(tmpElec)] = use[i]
            elecCnt[use[i]] -= 1
            cnt += 1

print(cnt)