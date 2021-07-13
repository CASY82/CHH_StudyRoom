#kakao internship
#프로그래밍 1번(세금 정책) -- 테스트 케이스는 통과!

money = 1000000000
minratio = 50
maxratio = 99
ranksize = 100000
threshold = 0
months = 6


def solution(money, minratio, maxratio, ranksize, threshold, months):
    rank = 0

    if threshold > money:
        return money

    for j in range(months):
        for i in range(minratio, maxratio+1):
            if (threshold + (rank * ranksize) <= money) and (threshold + ((rank+1) * ranksize - 1) > money):
                money_so = int(money / 100) * 100
                money_so = money_so * (i/100)
                money = int(money - money_so)
                rank = 0
                break
            else:
                if (threshold + ((rank+1) * ranksize - 1) < money) and (i == maxratio):
                    money_so = int(money / 100) * 100
                    money_so = money_so * (i / 100)
                    money = int(money - money_so)
                    rank = 0
                else:
                    rank += 1



    return money

print(solution(money, minratio, maxratio, ranksize, threshold, months))
