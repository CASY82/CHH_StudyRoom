# ad 제거하기

def solution(strArr):
    answer = []

    for word in strArr:
        if "ad" not in word:
            answer.append(word)

    return answer

tmp = ["and","notad","abcd"]
print(solution(tmp))