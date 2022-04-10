n = 9
k = 3

from collections import deque

# visited를 구현했으면.... DP형태로 풀었다면 시간초과가 없었을것 같음
def bfs(x, n, k):
    que = deque()
    que.append((x, x, 1))
    cnt = 0

    while que:
        tx, location, jump = que.popleft()

        if location == n and k == jump:
            cnt += 1
            continue

        if jump < k:
            for i in range(1, tx):
                if location + i <= n:
                    que.append((i, location + i, jump + 1))

    return cnt % 1000000007

def solution(n, k):
    answer = 0
    cnt = [0]
    # 최초 점프 시, 최소 토끼 굴 까지 거리를 k로 나눈 것 보다 커야 함
    distance = n // k + 1
    for i in range(distance, n):
        answer += bfs(i, n, k)

    if n == 1 and k == 1:
        answer = 1

    return answer

print(solution(n, k))