scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
#[[50,90],[50,87]]
#[[70,49,90],[68,50,38],[73,31,100]]

def solution(scores):
    result = ''

    for i in range(len(scores)):
        average = 0
        high_check = 0
        low_check = 100
        count = 0
        person = len(scores)

        for j in range(len(scores)):

            if high_check < scores[j][i]:
                high_check = scores[j][i]
            if low_check > scores[j][i]:
                low_check = scores[j][i]
            if j != i and scores[i][i] == scores[j][i]:
                count += 1

            average += scores[j][i]

        if (high_check == scores[i][i] or low_check == scores[i][i]) and count == 0:
            average -= scores[i][i]
            person -= 1

        average /= person

        print(average)

        if average >= 90:
            result += 'A'
        elif average >= 80:
            result += 'B'
        elif average >= 70:
            result += 'C'
        elif average >= 50:
            result += 'D'
        else:
            result += 'F'

    return result

print(solution(scores))