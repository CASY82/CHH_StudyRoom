dist = [[0,5,2,4,1],[5,0,3,9,6],[2,3,0,6,3],[4,9,6,0,3],[1,6,3,3,0]]
# dist = [[0,2,3,1],[2,0,1,1],[3,1,0,2],[1,1,2,0]]

def solution(dist):
    answer = []
    tmp = [0 for i in range(len(dist))]
    location = []

    #일단 0 기준으로 한번 위치를 잡아보자
    for v, i in enumerate(dist[0]):
        location.append((v, i))

    location.sort(key= lambda x:x[1], reverse=True)
    for i in range(len(location)):
        tmp[i] = location[i][0]

    #여기서 각 점들에 대한 위치를 돌면서 위치를 수정
    # for i in range(len(dist)):
    #     for j in range(len(dist)):
    #         if tmp[i]

    answer.append(tmp)
    answer.append(list(reversed(tmp)))
    answer.sort()

    return answer

print(solution(dist))