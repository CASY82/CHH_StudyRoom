#스택/큐 4번 주식가격

prices = [1, 2, 3, 2, 3]


def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i, price in enumerate(prices):
        # stack이 비었이면 false
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    # for문 다 돌고 Stack에 남아있는 값들 pop
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j

    return answer

print(solution(prices))


# 결국 효율성 테스트를 넘기지 못한....
# 큐를 이용한 풀이는 시간 초과가 나는 것을 알 수 있었다.


# def solution(prices):
#     answer = []
#     time = 0
#
#     while len(prices):
#         if prices[0] > prices[time] or time == (len(prices)-1):
#             answer.append(time)
#             prices.pop(0)
#             time = 0
#         else:
#             time += 1
#
#     return answer

# 대부분의 사람들이 푼 방식

# def solution(prices):
#     answer = [0] * len(prices)
#
#     for i in range(len(prices)-1):
#         for j in range(i, len(prices)-1):
#             if prices[i] >prices[j]:
#                 break
#             else:
#                 answer[i] +=1
#     return answer

# 스택 풀이 1

# def solution(prices):
#     # answer = 몇초 후 가격이 떨어지는지 저장하는 배열
#     answer = [len(prices) - i - 1 for i in range(len(prices))]
#
#     # stack = prices의 인덱스를 차례로 담아두는 배열
#     stack = [0]
#
#     for i in range(1, len(prices)):
#         while stack:
#             index = stack[-1]
#
#             # 주식 가격이 떨어졌다면
#             if prices[index] > prices[i]:
#                 answer[index] = i - index
#                 stack.pop()
#
#             # 떨어지지 않았다면 다음 시점으로 넘어감 (주식 가격이 계속 증가하고 있다는 말)
#             else:
#                 break
#
#         # 스택에 추가한다.
#         # 다음 시점으로 넘어갔을 때 다시 비교 대상이 될 예정이다.
#         stack.append(i)
#
#     return answer