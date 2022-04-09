import sys

path = "EEESEEEEEENNNN"
# path = "SSSSSSWWWNNNNNN"

def makeString(location, change, time, meter):
    change_direct = ""

    if location == "E":
        if change == "S":
            change_direct = "right"
        else:
            change_direct = "left"
    elif location == "S":
        if change == "E":
            change_direct = "left"
        else:
            change_direct = "right"
    elif location == "W":
        if change == "S":
            change_direct = "left"
        else:
            change_direct = "right"
    else:
        if change == "E":
            change_direct = "right"
        else:
            change_direct = "left"

    tmp_string = "Time " + str(time) + ": Go straight " + str(meter * 100) + "m and turn " + change_direct
    return tmp_string


def solution(path):
    answer = []

    i = 0
    # 일단 문자열 순회 시작
    while i < len(path)-5:
        start = path[i]
        tmp = path[i+1:i+6]
        # 현재 위치에서 500m 안쪽에서 변화를 감지
        for j in range(len(tmp)):
            # 앞 뒤가 변경 되는 시점을 찾아야 한다. 그게 유지 되면 거기서 더이상 연산 X
            if start != tmp[j]:
                answer.append(makeString(start, tmp[j], i, j + 1))
                start = tmp[j]
                i += j
                break

        i += 1

    return answer

print(solution(path))