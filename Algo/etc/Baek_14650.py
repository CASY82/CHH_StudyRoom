import sys

n = int(sys.stdin.readline())

# 백트래킹
def count_divisible_by_3(n):
    count = 0

    def generate(current_num, position, digit_sum):
        nonlocal count
        if position == n:  # n자리 수가 완성된 경우
            if digit_sum % 3 == 0:
                count += 1
            return

        # 다음 자리 숫자 선택
        for digit in [0, 1, 2]:
            if position == 0 and digit == 0:  # 첫 번째 자리는 0이 될 수 없음
                continue
            generate(current_num * 10 + digit, position + 1, digit_sum + digit)

    generate(0, 0, 0)  # 초기 호출
    return count

print(count_divisible_by_3(n))