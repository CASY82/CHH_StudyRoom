#20210911 9/30 2

research = ["abaaaa","aaa","abaaaaaa","fzfffffffa"]
n = 2
k = 2

# research = ["xy","xy"]
# n = 1
# k = 1

research = ["yxxy","xxyyy","yz"]
n = 2
k = 1

# research = ["yxxy","xxyyy"]
# n = 2
# k = 1


def solution(research, n, k):
    char_list = []
    char_count = []
    check = []

    for i in range(len(research)):
        for j in range(len(research[i])):
            if research[i][j] not in char_list:
                char_list.append(research[i][j])

    char_list.sort()
    result = [0 for i in range(len(char_list))]

    for i in range(len(research)):
        for j in range(len(char_list)):
            char_count.append(research[i].count(char_list[j]))

    for i in range(len(char_count)):
        for j in range(len(char_list)):
            if i % len(char_list) == j:
                result[j] += char_count[i]

                if char_count[i] > k and char_count[i] != 0:
                    check.append(char_list[j])

    for i in range(len(result)):
        if result[i] >= n * 2 * k:
            if check.count(char_list[i]) >= n:
                answer = char_list[i]
                break
            else:
                answer = 'None'
        else:
            answer = 'None'

    return answer

print(solution(research, n, k))