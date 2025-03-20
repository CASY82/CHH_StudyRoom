import sys

def second_largest_values(input_dict):
    # value를 리스트로 변환하고 중복 제거 후 정렬
    unique_values = sorted(set(input_dict.values()), reverse=True)

    # 두 번째로 큰 값 찾기
    if len(unique_values) < 2:
        return []  # 두 번째로 큰 값이 없을 경우 빈 리스트 반환

    second_largest = unique_values[1]

    # 두 번째로 큰 값에 해당하는 키들을 리스트로 모으기
    result = [key for key, value in input_dict.items() if value == second_largest]

    return result

while True:
    n, m = map(int, sys.stdin.readline().split())

    if n == m == 0:
        break

    player = dict()

    for i in range(n):
        ranker = list(map(int, sys.stdin.readline().split()))

        for j in range(m):
            if ranker[j] not in player:
                player[ranker[j]] = 1
            else:
                player[ranker[j]] += 1

    tmp = second_largest_values(player)
    tmp.sort()

    print(*tmp)