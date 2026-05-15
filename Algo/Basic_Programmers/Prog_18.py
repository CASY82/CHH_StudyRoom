# 왼쪽 오른쪽

def solution(str_list):
    answer = []

    for i in range(len(str_list)):
        if "l" == str_list[i]:
            answer = str_list[:i]

            break
        elif "r" == str_list[i]:
            answer = str_list[i + 1:]

            break

    return answer

print(solution(["u", "u", "l", "r"]))
print(solution(["l"]))
print(solution(["u", "u"]))
print(solution(["u", "u", "r", "r", "r"]))
print(solution(["u", "u", "r", "l", "r", "r", "r", "r"]))