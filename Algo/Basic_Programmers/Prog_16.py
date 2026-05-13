# 5명씩

def solution(names):
    answer = []

    for i in range(0, len(names), 5):
        answer.append(names[i])

    return answer

print(solution(["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]))