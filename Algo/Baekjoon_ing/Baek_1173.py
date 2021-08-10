#전체적인 로직은 동일하였으나, 반례의 상황을 다른사람 코드를 좀 인용하였다.

N, m, M, T, R = map(int, input().split())

X = m
time = 0

while N != 0:
    #찾지 못한 반례, 이 부분은 전혀 모르겠어서 다른사람의 도움을 받았다.
    if m + T > M:
        time = -1
        break

    if X + T <= M:
        X += T
        N -= 1
    else:
        X -= R
        if X < m:
            X = m

    time += 1

print(time)