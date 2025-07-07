import sys

t = int(sys.stdin.readline())

for case in range(1, t + 1):
    n, m = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))

    count = 0  # 합이 M인 쌍의 개수
    left = 0  # 왼쪽 포인터
    right = n - 1  # 오른쪽 포인터

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == m:
            count += 1
            left += 1
            right -= 1
        elif current_sum < m:
            left += 1  # 합이 작으므로 왼쪽 값을 늘려야 함
        else:  # current_sum > M
            right -= 1  # 합이 크므로 오른쪽 값을 줄여야 함

    print("Case #{0}: {1}".format(case, count))