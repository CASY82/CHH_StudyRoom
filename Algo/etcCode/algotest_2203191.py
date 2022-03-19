goods = ["pencil","cilicon","contrabase","picturelist"]

def sol(strings):
    result = []
    for i in range(1, len(strings)+1):
        for j in range(i):
            result.append(strings[j:j+len(strings)-i+1])
    return result

def solution(goods):
    answer = []
    tmp = []

    # 부분 문자열 다 구하기
    for product in goods:
        tmp.append(sol(product))

    for word in range(len(tmp)):
        result = set()
        check = True
        for part_word in tmp[word]:
            for i in range(len(tmp)):
                if word == i:
                    continue
                if part_word in tmp[i]:
                    check = False

            if check:
                result.add(part_word)

        answer.append(result)

    return answer


print(solution(goods))
