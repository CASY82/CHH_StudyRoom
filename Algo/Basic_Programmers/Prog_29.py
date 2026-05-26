# 세로 읽기

def solution(my_string, m, c):
    length = len(my_string)
    p = length // m
    tmp = [["" for _ in range(m)] for _ in range(p)]
    index = 0

    for i in range(p):
        for j in range(m):
            tmp[i][j] = my_string[index]
            index += 1

    ans = ""

    for k in range(p):
        ans += tmp[k][c - 1]

    return ans

print(solution("ihrhbakrfpndopljhygc", 4, 2))
print(solution("programmers", 1, 1))