# 20210911 9/30 3 못풀겠습니다.

import heapq

jobs = [[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]]
result = [2, 1, 2, 3]

def solution(jobs):
    result = []
    work = []
    new_work = []
    time = 0
    process_time = 0

    while time < 18:
        time += 1
        process_time += 1

        for i in range(len(jobs)):
            if time == jobs[i][0]:
                heapq.heappush(new_work, jobs[i][2])

                if not work:
                    work.append(heapq.heappop(new_work))

            if process_time == jobs[i][1]:
                result.append(work.pop())
                process_time = 0

        print(work ,time)
        print(new_work)

    return result

print(solution(jobs))