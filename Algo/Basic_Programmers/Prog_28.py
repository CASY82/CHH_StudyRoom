# 둘만의 암호

def solution(s, skip, index):
    answer = ''
    skip_word = list(skip)
    alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")

    for w in skip_word:
        alpha.remove(w)

    alpha_len = len(alpha)

    for i in range(len(s)):
        answer = answer + alpha[(alpha.index(s[i]) + index) % alpha_len]

    return answer

print(solution("aukks", "wbqd", 5))