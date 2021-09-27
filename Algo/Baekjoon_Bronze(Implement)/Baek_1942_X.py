# time = []
#
# for i in range(3):
#     time.append(input().split())
#
# for i in range(3):
#     start, end = int(''.join(time[i][0].split(':'))), int(''.join(time[i][1].split(':')))
#     count = 0
#
#     print(start, end)


# 다른사람 풀이 참고(이 문제는 너무 노가다를 하지 않으면 당최 어떤식으로 풀어야 하는지 감도 잡기 어려웠다.)
import datetime
from datetime import timedelta

for i in range(3):
    start, end = input().split()

    st = int(start.replace(":", ""))
    ed = int(end.replace(":", ""))

    stH, stM, stS = map(int, start.split(":"))
    edH, edM, edS = map(int, end.split(":"))

    stime = datetime.datetime(2021, 1, 1, stH, stM, stS)

    tmp_time = stime.strftime('%H%M%S')

    # 1씩 더하기 때문
    sec = 1

    cnt = 0
    if int(tmp_time) % 3 == 0:
        cnt += 1
    etime = datetime.datetime(2021, 1, 1, edH, edM, edS)
    etime = etime.strftime('%H%M%S')

    while True:
        if tmp_time == etime:
            break

        # sec만큼 증가 (여기서 sec은 1)
        stime = stime + timedelta(seconds=sec)
        tmp_time = stime.strftime('%H%M%S')
        if int(tmp_time) % 3 == 0:
            cnt += 1

    print(cnt)