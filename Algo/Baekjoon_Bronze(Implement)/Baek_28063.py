# 동전 복사

# 1. n = 1 는 0
# 2. n = 2 는 2
# 3. n = 3부터 모서리는 2, 변 가운데는 3 정 가운데는 4

n = int(input())
x, y = map(int, input().split())

ans = (1 if x > 1 else 0) + (1 if x < n else 0) + (1 if y > 1 else 0) + (1 if y < n else 0)
print(ans)