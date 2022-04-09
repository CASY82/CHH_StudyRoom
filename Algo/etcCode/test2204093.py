tstring = "this is {template} {template} is {state}"
# variables = [["template", "string"], ["state", "changed"]]

# variables = [["template", "string"], ["state", "{template}"]]
variables = [["template", "{state}"], ["state", "{templates}"]]


from collections import deque

#트리인지 확인하는 문제 였다. 트리가 아닌 사이클이 발생하면 종료하도록 하면 됨(시험 시간이....)

def bfs(tstring, variables):
    que = deque()
    que.append(tstring)
    visited = [True for _ in range(len(variables))]

    while que:
        variable_text = que.popleft()

        if variable_text[0] == "{":
            for i in range(len(variables)):
                if variables[i][0] in variable_text and visited[i]:
                    visited[i] = False
                    que.append(variables[i][1])
        else:
            return variable_text


def solution(tstring, variables):
    answer = ''
    result = []

    tmp = tstring.split()

    # 일단은 치환부터 한다.
    for i in tmp:
        if i[0] == "{":
            # for j in range(len(variables)):
            #     if variables[j][0] in i:
            #         result.append(variables[j][1])
            #         break
            text = bfs(i, variables)
            if text == None:
                result.append(i)
            else:
                result.append(text)
        else:
            result.append(i)

    print(result)

    answer = ' '.join(result)

    return answer

print(solution(tstring, variables))