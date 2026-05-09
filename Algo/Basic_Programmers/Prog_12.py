# 문자 개수 세기

def solution(my_string):
    answer = [0] * 52

    for i in range(len(my_string)):
        tmp = ord(my_string[i])
        if 65 <= tmp <= 90:
            answer[tmp - 65] += 1
        else:
            answer[tmp - 71] += 1

    return answer

print(solution("Programmers"))
# print(solution("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"))