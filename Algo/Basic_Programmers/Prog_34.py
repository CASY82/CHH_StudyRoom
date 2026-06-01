# 9로 나눈 나머지

def solution(number):
    tmp = 0

    for i in range(len(number)):
        tmp += int(number[i])

    return tmp % 9

print(solution("123"))
print(solution("78720646226947352489"))