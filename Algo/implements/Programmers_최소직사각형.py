sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]

def solution(sizes):
    answer = 0

    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]

    tmp_0 = sorted(sizes, key = lambda x:x[0], reverse=True)
    tmp_1 = sorted(sizes, key = lambda x:x[1], reverse=True)
    print(tmp_0)
    print(tmp_1)

    answer = tmp_0[0][0] * tmp_1[0][1]

    return answer

print(solution(sizes))

#한줄 풀이가 가능했다...
# def solution(sizes):
#     return max(max(x) for x in sizes) * max(min(x) for x in sizes)