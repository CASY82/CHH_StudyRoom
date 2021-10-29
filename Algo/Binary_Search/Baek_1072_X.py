# if x == y:
#     print(-1)
# else:
    # 맞긴한데.. 시간초과 날듯
    # while True:
    #     win_rate = int((y / x) * 100)
    #
    #     if win_rate != first_win_rate:
    #         break
    #
    #     count += 1
    #     y += 1
    #     x += 1
# binary search로 다시 구현해보자
# 아래 참고 소스와 반례를 확인 후 비교 대조하여 풀었다.
x, y = map(int, input().split())
target_win_rate = int((y*100) / x)

start = 1
end = 1000000000
ans = 0

if target_win_rate >= 99:
    print(-1)
else:
    while True:
        mid = (start + end) // 2

        win_rate = int(((y + mid) * 100 / (x + mid)))

        if start > end:
            break

        if win_rate > target_win_rate:
            end = mid - 1
            ans = mid
        elif win_rate <= target_win_rate:
            start = mid + 1

    print(ans)


#아래는 다른사람 풀이 참고
# from math import floor
# import sys
# input = sys.stdin.readline
# x, y = map(int, input().split())
# e = floor(100 * y / x)
# low, high = 0, 1000000000
# if e >= 99: print(-1)
# else:
#     while low <= high:
#         mid = (low + high) // 2
#         tx, ty = x + mid, y + mid
#         if floor(100 * ty / tx) > e: high = mid - 1
#         else: low = mid + 1
#     print(high + 1)