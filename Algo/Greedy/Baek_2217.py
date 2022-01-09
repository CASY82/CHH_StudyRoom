import sys

n = int(sys.stdin.readline())

# 로직은 다음과 같다.
# 1. 정렬
# 2. 제일 큰 수가 들수 있는 무게 확인
# 3. 그 다음 큰 수를 선택하고 해당 무게의 * 2
# 4. 그 다음 큰 수를 선택하고 해당 무게의 * 3
# 5. 위와 같은 방법으로 가장 작은 무게까지 확인을 하는데, 그 중 무게가 가장 많이 나가는 친구를 고르면 된다.

weight = []
for _ in range(n):
    weight.append(int(sys.stdin.readline()))

weight.sort(reverse=True)
result = 0

for i in range(len(weight)):
    if result < weight[i] * (i+1):
        result = weight[i] * (i+1)

print(result)
