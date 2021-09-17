#2021/08/14 to test ss 1

servers = 2;
sticky = False;
requests = [1, 2, 3 ,4]

def solution(servers, sticky, requests):
    request_list = []
    answer = []
    count = 0

    for i in range(len(requests)):
        list = []

        for j in requests:
            if requests.index(j) % servers == count:
                list.append(j)
                request_list.append(j)

        set(request_list)

        #아직 내 실력으로 sticky는 너무 오래걸린다.
        if sticky == True:
            pass
        else:
            answer.append(list)
        count += 1

        if count == servers:
            break

    return answer



print(solution(servers, sticky, requests))