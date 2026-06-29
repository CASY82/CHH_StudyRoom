# 코드 처리하기

def solution(code):
    answer = ''
    mode = 0

    for i in range(len(code)):
        if code[i] == "1":
            mode = int(not mode)
        else:
            if mode == 0 and i % 2 == 0:
                answer = answer + code[i]
            elif mode == 1 and i % 2 == 1:
                answer = answer + code[i]

    if answer == "":
        return "EMPTY"

    return answer

print(solution("abc1abc1abc"))