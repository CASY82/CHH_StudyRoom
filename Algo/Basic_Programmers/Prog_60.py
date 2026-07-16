# 이진수 더하기

def solution(bin1, bin2):
    decimal_num = int(bin1, 2) + int(bin2, 2)

    return bin(decimal_num)[2:]

print(solution("10", "11"))
print(solution("1001", "1111"))