import sys

s, p = map(int, sys.stdin.readline().split())
dna = sys.stdin.readline().strip()
min_counts = list(map(int, input().split()))


def count_valid_passwords(dna, p_length, min_counts):
    from collections import Counter

    # DNA 문자열 길이
    s_length = len(dna)

    # 슬라이딩 윈도우 초기화
    current_count = Counter(dna[:p_length])
    valid_password_count = 0

    # 조건을 만족하는지 확인하는 함수
    def is_valid(counts, min_counts):
        return (counts['A'] >= min_counts[0] and
                counts['C'] >= min_counts[1] and
                counts['G'] >= min_counts[2] and
                counts['T'] >= min_counts[3])

    # 처음 부분 문자열 검사
    if is_valid(current_count, min_counts):
        valid_password_count += 1

    # 슬라이딩 윈도우 진행
    for i in range(p_length, s_length):
        # 새 문자 추가
        current_count[dna[i]] += 1
        # 이전 문자 제거
        current_count[dna[i - p_length]] -= 1

        # 0 이하로 떨어진 경우 제거
        if current_count[dna[i - p_length]] == 0:
            del current_count[dna[i - p_length]]

        # 현재 부분 문자열 검사
        if is_valid(current_count, min_counts):
            valid_password_count += 1

    return valid_password_count

print(count_valid_passwords(dna, p, min_counts))