import sys

n = int(sys.stdin.readline())

cards = list(map(int, sys.stdin.readline().split()))

def min_payment_for_cards(cards, n):
    # 무한대로 초기화
    dp = [float('inf')] * (n + 1)
    # 카드가 0개일때는 당연히 방법도 0
    dp[0] = 0

    #i는 카드의 개수에 대한 순회
    #j는 카드 가격에 대한 순회
    for i in range(1, n + 1):
        for j in range(len(cards)):
            #현재 고려중인 카드 개수가 인덱스에 해당하는 카드의 가격 갯수를 뺀 값보다 큰 경우에만 계산
            if i - (j + 1) >= 0:
                dp[i] = min(dp[i], dp[i - (j + 1)] + cards[j])

    return dp[n]

print(min_payment_for_cards(cards, n))

# 다른 사람 풀이
# N = int(input())
# P = list(map(int, input().split()))
#
# P = [(i+1, v) for i, v in enumerate(P)]
#
# dp = [float('inf')]*(N+1)
# dp[0] = 0
#
# for i in range(1,len(P)+1):
#     n,p = P[i-1] #n개카드, 팩당가격
#
#     for j in range(n,N+1):
#         dp[j] = min( dp[j], dp[j-n]+p )
#
# print(dp[N])

# 다른 사람 풀이 2
#
# N = int(input())
# p = [0] + list(map(int,input().split()))
# dp = [0 for _ in range(N+1)]
#
#
# for i in range(1,N+1):
#     for k in range(1,i+1):
#         dp[i] = max(dp[i], dp[i-k] + p[k])
# print(dp[i])