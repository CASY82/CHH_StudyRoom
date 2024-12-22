import sys

n = int(sys.stdin.readline())

#한자리 1~9 -> 9를 차지
#두자리 10~99 100개 --> 180(길이)
#세자리 100~999 1000개 --> 2700

# test = 0
#
# for i in range(1, 9):
#     test += (i * (10 ** (i - 1))) * 9
#
#     print(test)

if n >= 10:
    jari = [0, 9, 189, 2889, 38889, 488889, 5888889, 68888889, 788888889]
    num_length = 0

    for case in range(len(jari) - 1):
        # n이 속해있는 수의 범위(예를 들어 9에서 189면은 두 자리수가 그제서야 끝나는거고 n은 몇번째 자리인가를 나타낼뿐
        if jari[case] < n <= jari[case + 1]:
            num_length = case + 1
            break

    start_num = 10 ** (num_length - 1)
    end_num = 10 ** num_length
    # 자릿수가 이전인 수까지는 문자열의 길이에서 빼야함
    tmp_jari_num = n - jari[num_length - 1]
    # 그럼 start_num의 수(자릿수) 를 기준으로 나눠주면 몇번째 숫자인지 나오고, 나머지는 그 숫자의 몇번째 수인지 알 수 있다.
    if tmp_jari_num % num_length == 0:
        tmp_num_find = str((tmp_jari_num // num_length) - 1 + start_num)
    else:
        tmp_num_find = str((tmp_jari_num // num_length) + start_num)
    tmp_num_remain = tmp_jari_num % num_length - 1

    print(tmp_num_find[tmp_num_remain])
else:
    print(n)

# 다른 사람 풀이
# def find_nth_digit(N):
#     # 1. 자릿수별로 숫자의 개수를 계산
#     # 1자리: 1-9 (9개)
#     # 2자리: 10-99 (90개)
#     # 3자리: 100-999 (900개)
#     if N < 10:
#         return str(N)
#
#     length = 1  # 현재 숫자의 자릿수
#     count = 9  # 현재 자릿수의 숫자 개수
#     start = 1  # 현재 자릿수의 시작 숫자
#
#     # N번째 숫자가 몇 자리 숫자에 속하는지 찾기
#     total_digits = 0  # 누적 자릿수
#     while total_digits + length * count < N:
#         total_digits += length * count
#         length += 1
#         count *= 10
#         start *= 10
#
#     # N번째 숫자가 속한 실제 숫자 찾기
#     offset = N - total_digits - 1
#     num = start + offset // length  # 실제 숫자
#     digit_index = offset % length  # 숫자 내에서의 위치
#
#     return str(num)[digit_index]
#
#
# # 입력 받기
# N = int(input())
# print(find_nth_digit(N))