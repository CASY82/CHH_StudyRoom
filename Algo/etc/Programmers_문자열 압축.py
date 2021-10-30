# s = "aabbaccc"
s = "ababcdcdababcdcd"
# s = "abcabcdede"
# s = "abcabcabcabcdededededede"
# s = "xababcdcdababcdcd"
# s = "a"

def solution(s):
    answer = 0
    result = []

    if len(s) > 1:
        for i in range(1, len(s)):
            length = i

            # checker = list(map(''.join, zip(*[iter(s)] * length)))
            checker = [s[i:i+length] for i in range(0, len(s), length)]

            # print(checker)

            check_word = checker[0]
            count = 1
            new_word = ''

            if ''.join(checker) == s:
                if len(checker) >= 2:
                    for j in range(1, len(checker)):
                        if check_word == checker[j]:
                            count += 1
                        else:
                            if count > 1:
                                new_word += str(count)
                            new_word += check_word
                            check_word = checker[j]
                            count = 1

                    if j == (len(checker) - 1):
                        if count > 1:
                            new_word += str(count)
                        new_word += check_word

                    # print(new_word)

                if s != new_word:
                    result.append(len(new_word))
    else:
        result.append(len(s))

    if result:
        answer = min(result)
    else:
        answer = len(new_word)


    return answer

print(solution(s))