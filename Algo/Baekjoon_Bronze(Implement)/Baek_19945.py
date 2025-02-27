def count_bits(n):
    if n == 0:
        return 1  # 0은 1비트를 사용
    elif n < 0:
        n = (1 << 32) + n  # 음수를 2의 보수로 변환

    # 이진수 문자열로 변환 후 앞의 0 제거
    binary_representation = bin(n)[2:]  # '0b' 접두사 제거
    return len(binary_representation)  # 비트 수 반환

# 입력 받기
n = int(input())

# 비트 수 출력
print(count_bits(n))
