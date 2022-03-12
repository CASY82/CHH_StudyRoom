import sys

# money = 4578
# costs = [1, 4, 99, 35, 50, 1000]

money = 1999
costs = [2, 11, 20, 100, 200, 600]

def solution(money, costs):
    answer = 0

    coin = [1, 5, 10, 50, 100, 500]

    while money > 0:
        minCost = 1000001
        tmpCoin = 0
        for i in range(len(coin)):
            tmp = money / coin[i]

            if minCost > costs[i] * tmp and int(tmp) != 0:
                minCost = costs[i] * int(tmp)
                tmpCoin = coin[i] * int(tmp)

        answer += minCost
        money -= tmpCoin


    return answer

print(solution(money, costs))