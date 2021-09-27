# info = [[1,5], [3,5], [7,8]]
# info = [[2,3], [2,5], [2,2], [3,3]]
info = [[1,2], [2,3], [4,5], [5,6]]

def solution(info):
    counter = [0] * (max(map(max, info)) + 1)

    for i in range(len(info)):
        for j in range(info[i][0], info[i][1] + 1):
            counter[j] += 1

    answer = list(filter(lambda x: counter[x] == max(counter), range(len(counter))))

    return answer

print(solution(info))