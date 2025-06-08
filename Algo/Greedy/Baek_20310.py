import sys

def get_smallest_half_binary_string(s):
    """
    주어진 0과 1로 이루어진 문자열에서 절반의 길이를 갖는 사전순 최소 문자열을 생성합니다.
    1은 앞에서부터 절반을 제거하고, 0은 뒤에서부터 절반을 제거합니다.
    입력 문자열은 0과 1의 개수가 각각 짝수임을 가정합니다.

    Args:
        s: 0과 1로 이루어진 문자열.

    Returns:
        규칙에 따라 재구성된 절반 길이의 문자열.
    """
    # 문제 제약조건에 따라 입력 문자열 길이는 항상 짝수이고, 0과 1의 개수도 각각 짝수입니다.
    num_zeros = s.count('0')
    num_ones = s.count('1')

    # 남겨야 할 문자의 개수 계산
    keep_zeros = num_zeros // 2
    keep_ones = num_ones // 2

    # 남길 문자의 원래 인덱스를 저장할 리스트
    kept_indices = []

    # 원래 문자열에서 모든 '0'과 '1'의 인덱스를 찾습니다.
    zero_indices = [i for i, char in enumerate(s) if char == '0']
    one_indices = [i for i, char in enumerate(s) if char == '1']

    # 남겨야 할 '0'은 앞에서부터 keep_zeros개 입니다.
    kept_indices.extend(zero_indices[:keep_zeros])

    # 남겨야 할 '1'은 뒤에서부터 keep_ones개 입니다.
    # 파이썬 슬라이싱 [-k:]는 리스트의 마지막 k개 요소를 가져옵니다.
    kept_indices.extend(one_indices[-keep_ones:])

    print(kept_indices)

    # 남기기로 결정된 인덱스들을 원래 문자열에서의 순서대로 정렬합니다.
    kept_indices.sort()

    # 정렬된 인덱스를 사용하여 최종 문자열을 구성합니다.
    result = "".join(s[i] for i in kept_indices)

    return result

# 예시 실행
print(get_smallest_half_binary_string(sys.stdin.readline().strip()))