s = 'baabaa'
# s = 'cdcd'

def solution(s):
    answer = 1
    stack = []

    for i in range(len(s)):
        stack.append(s[i])

        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()

    if stack:
        answer = 0

    return answer

print(solution(s))