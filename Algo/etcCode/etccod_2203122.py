n = 5
clockwise = True

def recursion(num, start, end, array, clockwise):

    # 각 끝 시작 지점
    array[start][start] = num
    array[start][end] = num
    array[end][end] = num
    array[end][start] = num

    # mid에 들어가는 숫자
    mid = [i for i in range(num + 1, (num + 1)+(end-start-1))]

    # 제일 가운데인 경우 mid가 더이상 없으므로 함수 탈출
    if len(mid) == 0:
        return

    # 방향
    midStart = mid[-1] + 1
    if not clockwise:
        mid.reverse()

    # 가운데 부분 채우기
    tmpArray = [j for j in range(start+1, end)]
    for (m, a) in enumerate(tmpArray):

        # 두 위치와는 반대로 돌아야 하므로
        reverseA = len(array)-a-1

        # 위
        array[start][a] = mid[m]

        # 오른쪽
        array[a][end] = mid[m]

        # 아래
        array[end][reverseA] = mid[m]

        # 왼쪽
        array[reverseA][start] = mid[m]

    recursion(midStart, start+1, end-1, array, clockwise)


def solution(n, clockwise):
    answer = [[0 for _ in range(n)] for _ in range(n)]

    num = 1
    start = 0
    end = n - 1

    recursion(num, start, end, answer, clockwise)

    return answer

print(solution(n, clockwise))