# lottos = [44, 1, 0, 0, 31, 25]
# win_nums = [31, 10, 45, 1, 6, 19]

# lottos = [0, 0, 0, 0, 0, 0]
# win_nums = [38, 19, 20, 40, 15, 25]

# lottos = [45, 4, 35, 20, 3, 9]
# win_nums = [20, 9, 3, 45, 4, 35]

lottos = [1, 2, 6, 22, 21, 19]
win_nums = [20, 9, 3, 45, 4, 35]


def solution(lottos, win_nums):
    answer = []
    rate = [6, 6, 5, 4, 3, 2, 1]
    counter = 0

    for j in range(len(lottos)):
        if lottos[j] in win_nums:
            counter += 1

#if문이 따로 필요 없었다...
    if counter == 0:
        answer.append(rate[lottos.count(0)])
        answer.append(rate[1])
    else:
        answer.append(rate[counter + lottos.count(0)])
        answer.append(rate[counter])

    return answer

print(solution(lottos, win_nums))