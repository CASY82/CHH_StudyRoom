# qr code

def solution(q, r, code):
    answer = ''

    for i in range(len(code)):
        if i % q == r:
            answer = answer + code[i]

    return answer

print(solution(3, 1, "qjnwezgrpirldywt"))
print(solution(1, 0, "programmers"))