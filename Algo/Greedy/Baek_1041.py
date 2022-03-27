import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
select = []
result = 0

# n == 1일때 예외처리를 안했다.
if n == 1:
    result = sum(num) - max(num)
else:
    for i in range(3):
        select.append(min(num[i], num[-(i+1)]))

    select.sort()

    # 3개면을 가진 블록 개수 고정 : 4개 이므로 젤 큰수는
    result += select[-1] * 4

    # 2개면을 가진 블록 개수는 (n-2) * 4 + (n-1) * 4 개 이므로 중간 크기의 숫자는 3개면 + 2개면 블록 개수
    second = ((n-2) * 4 + (n-1) * 4 + 4)
    result += select[1] * second

    # 1개면은 전체 면 개수 - 2번째 수 면개수 - 젤큰 수 면 개수
    result += select[0] * ((n*n*5)-second-4)

print(result)
