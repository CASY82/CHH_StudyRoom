survey = ["AN", "CF", "MJ", "RT", "NA"]
choices	= [5, 3, 2, 7, 5]

def solution(survey, choices):
    answer = ''
    indicator = [0, 0, 0, 0, 0, 0, 0, 0] # RT, CF, JM, AN
    indicator_alp = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    selector = [0, 3, 2, 1, 0, 1, 2, 3]

    #점수 체킹
    for num in range(len(survey)):
        first = survey[num][0]
        second = survey[num][1]

        if 1 <= choices[num] <= 3:
            indicator[indicator_alp.index(first)] += selector[choices[num]]
        elif 5 <= choices[num] <= 7:
            indicator[indicator_alp.index(second)] += selector[choices[num]]

    #성격 유형
    if indicator[0] >= indicator[1]:
        answer += 'R'
    else:
        answer += 'T'

    if indicator[2] >= indicator[3]:
        answer += 'C'
    else:
        answer += 'F'

    if indicator[4] >= indicator[5]:
        answer += 'J'
    else:
        answer += 'M'

    if indicator[6] >= indicator[7]:
        answer += 'A'
    else:
        answer += 'N'

    return answer

print(solution(survey, choices))