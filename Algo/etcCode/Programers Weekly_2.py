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


#풀이 참고
# from collections import Counter
#
# def solution(scores):
#     def rank(score):
#         if score >= 90:
#             return 'A'
#         elif score >= 80:
#             return 'B'
#         elif score >= 70:
#             return 'C'
#         elif score >= 50:
#             return 'D'
#         else:
#             return 'F'
#     answer = ''
#     # transpose
#     for i in range(len(scores)):
#         for j in range(1, i+1):
#             scores[i][i-j], scores[i-j][i] = scores[i-j][i], scores[i][i-j]
#     avg = []
#     for i, s in enumerate(scores):
#         if (max(s) == s[i] or min(s) == s[i]) and Counter(s)[s[i]] == 1:
#             avg.append((sum(s) - s[i])/(len(s)-1))
#         else:
#             avg.append(sum(s)/len(s))
#
#     rank = ''.join(list(map(rank, avg)))
#     return rank
#
# from collections import Counter
# def solution(scores):
#     answer = ''
#
#     for idx, score in enumerate(list(map(list, zip(*scores)))):
#         length = len(score)
#         if Counter(score)[score[idx]] == 1 and (max(score) == score[idx] or min(score) == score[idx]):
#             del score[idx]
#             length -= 1
#
#         grade = sum(score) / length
#
#         if grade >= 90:
#             answer += 'A'
#         elif grade >= 80:
#             answer += 'B'
#         elif grade >= 70:
#             answer += 'C'
#         elif grade >= 50:
#             answer += 'D'
#         else:
#             answer += 'F'
#
#     return answer
#
#
# def solution(scores):
#     import statistics
#     def scoring(x):
#         if x >= 90:
#             return 'A'
#         elif 80 <= x < 90:
#             return 'B'
#         elif 70 <= x < 80:
#             return 'C'
#         elif 50 <= x < 70:
#             return 'D'
#         else:
#             return 'F'
#
#     scores = list(map(list, zip(*scores)))
#     students = len(scores)
#     answer = ''
#
#     for i in range(students):
#         maximum = max(scores[i])
#         minimum = min(scores[i])
#         if scores[i].count(maximum) == 1 and scores[i][i] == maximum:
#             answer += scoring((sum(scores[i])-scores[i][i])/(students-1))
#         elif scores[i].count(minimum) == 1 and scores[i][i] == minimum:
#             answer += scoring((sum(scores[i])-scores[i][i])/(students-1))
#         else:
#             answer += scoring(statistics.mean(scores[i]))
#
#     return answer

# solution = lambda scores: "".join(map(lambda m: "FDDCBAA"[max(int(sum(m) / len(m) / 10) - 4, 0)], map(lambda m: (m[0], *m[1]) if min(m[1]) <= m[0] <= max(m[1]) else m[1], ((s[i], s[:i] + s[i+1:]) for i, s in enumerate(zip(*scores))))))
