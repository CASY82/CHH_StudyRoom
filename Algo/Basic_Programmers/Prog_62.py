# 인덱스 바꾸기

def solution(my_string, num1, num2):
    str_list = list(my_string)

    str_list[num1], str_list[num2] = str_list[num2], str_list[num1]

    return "".join(str_list)

print(solution("hello", 1, 2))
print(solution("I love you", 3,6))
