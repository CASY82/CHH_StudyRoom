# import sys
#
# t = int(sys.stdin.readline())
#
# for case in range(t):
#     n = int(sys.stdin.readline())
#     names = [sys.stdin.readline().strip() for _ in range(n)]
#
#     cnt = 0
#
#     # 삽입 정렬 방식으로 카드 정렬
#     for i in range(1, n):
#         key = names[i]
#         j = i - 1
#         moves = 0  # 현재 이동 횟수 카운트
#
#         # key가 이전 카드보다 작을 경우, 이동
#         while j >= 0 and names[j] > key:
#             names[j + 1] = names[j]
#             j -= 1
#             moves += 1  # 이동 카운트 증가
#
#         names[j + 1] = key
#         cnt += moves  # 현재 카드를 정렬하기 위해 이동한 횟수를 전체 비용에 추가
#
#     print("Case #{0}: {1}".format(case + 1, cnt))

def calculate_sorting_cost(deck):
    cost = 0
    sorted_deck = []

    for card in deck:
        pos = len(sorted_deck)
        while pos > 0 and sorted_deck[pos - 1] > card:
            pos -= 1

        sorted_deck.insert(pos, card)

        if pos != len(sorted_deck) - 1:
            cost += 1

    return cost

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    deck = [input().strip() for _ in range(N)]

    cost = calculate_sorting_cost(deck)
    print(f"Case #{t}: {cost}")

# 다른 사람 풀이

# for t in range(1, int(input()) + 1):
#     n = int(input())
#     names = [input() for _ in range(n)]
#     res, now = 0, names[0]
#     for i in range(1, n):
#         if now > names[i]:
#             res += 1
#             continue
#         now = names[i]
#     print(f"Case #{t}: {res}")