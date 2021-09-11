# 20210911 2  1
# 테케 3 시간 초과... 이거 모르겠다 여기서 캇

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3

def solution(id_list, report, k):
    reporter = []
    reported = []
    report_count = []
    stop_account = []
    answer = [0 for i in range(len(id_list))]

    report = list(set(report))

    for i in range(len(report)):
        a, b = map(str, report[i].split(' '))
        reporter.append(a)
        reported.append(b)

    for i in range(len(id_list)):
        report_count.append(reported.count(id_list[i]))

    for i in range(len(report_count)):
        if report_count[i] >= k:
            stop_account.append(id_list[i])

    stop_account = list(set(stop_account))

    for i in range(len(reported)):
        for j in range(len(stop_account)):
            if reported[i] == stop_account[j]:
                answer[id_list.index(reporter[i])] += 1

    return answer

print(solution(id_list, report, k))