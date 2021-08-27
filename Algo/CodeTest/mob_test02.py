a = ["abab","bbaa","bababa","bbbabababbbaa"]

def front(char_a):
    return 'a' + char_a

def back(char_a):
    return 'a' + char_a

def add_b(char_a):
    return 'b' + char_a + 'b'

def check_char(char_a, origin_a):
    if origin_a == char_a:
        return True
    else:
        char_a = front(char_a)

def solution(a):
    result = [False] * len(a)

    for i in a:
        a_char = 'a'
        result[a.index(i)] = check_char(a_char, i)







print(solution(a))