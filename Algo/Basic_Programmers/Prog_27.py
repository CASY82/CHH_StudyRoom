# 문자열의 뒤의 n글자

def solution(my_string, n):
    return my_string[len(my_string) - n:]

print(solution("ProgrammerS123", 11))
print(solution("He110W0r1d", 5))