#실패

from collections import deque

arr = ["1","2","4","3","3","4","1","5"]
processes = ["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]
#
# arr = ["1","1","1","1","1","1","1"]
# processes = ["write 1 12 1 5 8","read 2 3 0 2","read 5 5 1 2","read 7 5 2 5","write 13 4 0 1 3","write 19 3 3 5 5","read 30 4 0 6","read 32 3 1 5"]

# 두개의 queue를 만듦(read, write)
# 작업 큐를 하나더 만듦
# 작업 큐에 read가 있는 경우 시간 대 별로 동시 처리
# 작업 큐의 read가 전부 끝났을 때, write 가 있다면 write 처리
# 어떤 작업이든 작업 큐 처리가 끝났을 때 write가 있다면 write처리

def solution(arr, processes):
    answer = []
    wait_que = deque()
    processing_que = deque()
    whole_process = deque()
    time = 1
    result = 0

    for process in processes:
        whole_process.append(list(process.split()))

    while True:
        if whole_process and int(whole_process[0][1]) == time:
            tmp_process = whole_process.popleft()

            if not processing_que:
                processing_que.append(tmp_process)

            else:
                if processing_que[0][0] == "read" and tmp_process[0] == "read" and not wait_que:
                    processing_que.append(tmp_process)
                else:
                    wait_que.append(tmp_process)

        if int(processing_que[0][1]) + int(processing_que[0][2]) == time:
            using_process = processing_que.popleft()

            if using_process[0] == "read":
                answer.append(''.join(arr[int(using_process[3]):int(using_process[4])+1]))
            else:
                for i in range(int(using_process[3]), int(using_process[4])+1):
                    arr[i] = using_process[-1]

        wait_que = deque(sorted(wait_que, reverse=True, key=lambda x:x[0]))
        if not processing_que and wait_que and int(wait_que[0][1]) <= time:
            wait_que[0][1] = str(time)
            processing_que.append(wait_que.popleft())

        if not whole_process and not wait_que and not processing_que:
            break

        print(time)
        print('w', whole_process)
        print('wa', wait_que)
        print('p', processing_que)
        print()

        if processing_que:
            result += 1

        time += 1


    answer.append(str(result-1))

    return answer

print(solution(arr, processes))