#20210911 9/30 1(제출 완료) 테스트는 통과... 이후는 모르겠다

student = [0, 1, 0]
k = 2

def solution(student, k):
    count = 0


    for i in range(len(student)):
        one_count = 0
        for j in range(i, len(student)):
            if student[j] == 1:
                one_count += 1

            if one_count == k:
                count += 1

    return count

print(solution(student, k))

