# import sys
#
# t = int(sys.stdin.readline())
#
# for case in range(1, t + 1):
#     pattern = sys.stdin.readline().strip()
#     i, j = map(int, sys.stdin.readline().split())
#
#     pattern_len = len(pattern)
#     b_cnt = pattern.count("B")
#
#     start = i % pattern_len - 1
#     end = j % pattern_len
#
#     complete = ((j - end) - (i + start)) // pattern_len
#
#     res = complete * b_cnt + (pattern[start:].count("B") + pattern[:end].count("B"))
#     print("Case #{0}: {1}".format(case, res))

import sys

t = int(sys.stdin.readline())

for case in range(1, t + 1):
    pattern = sys.stdin.readline().strip()
    i, j = map(int, sys.stdin.readline().split())

    pattern_len = len(pattern)
    b_cnt = pattern.count("B")

    # 0-based 인덱싱을 위해 -1
    i -= 1
    j -= 1

    # 시작 패턴 조각
    start_partial_len = pattern_len - (i % pattern_len)
    # 실제 시작~끝 길이
    total_len = j - i + 1

    # 중간에 들어가는 전체 패턴 수
    if total_len <= start_partial_len:
        # 범위가 한 패턴도 못 채움
        segment = pattern[i % pattern_len : (i % pattern_len) + total_len]
        res = segment.count("B")
    else:
        res = 0
        # 앞쪽 조각
        start_segment = pattern[i % pattern_len:]
        res += start_segment.count("B")

        # 가운데 완전 패턴 반복
        remaining_len = total_len - len(start_segment)
        full_patterns = remaining_len // pattern_len
        res += full_patterns * b_cnt

        # 뒤쪽 조각
        end_len = remaining_len % pattern_len
        end_segment = pattern[:end_len]
        res += end_segment.count("B")

    print(f"Case #{case}: {res}")
