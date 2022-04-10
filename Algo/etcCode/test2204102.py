stats = [5, 3, 4, 6, 2, 1]

def solution(stats):
    answer = 0

    team = []

    team.append([stats[0]])

    for i in range(1, len(stats)):
        check = True
        for j in range(len(team)):
            if team[j][-1] < stats[i]:
                team[j].append(stats[i])
                check = False
                break

        if check:
            team.append([stats[i]])

    answer = len(team)

    return answer

print(solution(stats))