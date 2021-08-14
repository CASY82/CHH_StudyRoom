#2021/08/14 to test ss 2
#시간 초과

# fruitWeights = [30, 40, 10, 20, 30]
# k = 3

fruitWeights = [10, 20, 30, 40, 50]
k = 2

def solution(fruitWeights, k):
    answer = []


    for i in range(len(fruitWeights)):
        semi_list = []
        for j in range(i, k + i):
            if k + i > len(fruitWeights):
                break
            semi_list.append(fruitWeights[j])

        if k + i > len(fruitWeights):
            break

        answer.append(max(semi_list))

    return sorted(list(set(answer)), reverse=True)

print(solution(fruitWeights, k))