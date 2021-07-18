#힙 1번 더 맵게

scoville = [1, 2, 3, 9, 10, 12]
K = 7

import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while len(scoville) >= 2:
        min = heapq.heappop(scoville)

        if min >= K:
            return answer
        else:
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min + (min2 *2))
            answer += 1

    if scoville[0] > K:
        return answer
    else:
        return -1



    return answer


print(solution(scoville, K))

#결국 다른 사람의 풀이를 참고

#첫 도전 33점...
# def solution(scoville, K):
#     answer = 0
#
#     while True:
#         if scovile and scoville[0] < K and scoville[1] < K:
#             tmp1 = scoville.pop(0)
#             tmp2 = scoville.pop(0)
#
#             result = tmp1 + (tmp2 * 2)
#             scoville.append(result)
#
#             scoville.sort()
#
#             answer += 1
#         else:
#             break
#
#
#
#     return answer