# 첫 번째로 나오는 음수

def solution(array):
    tmp = "".join(map(str,array))

    return tmp.count("7")

print(solution([7, 77, 17]))
print(solution([10, 29]))