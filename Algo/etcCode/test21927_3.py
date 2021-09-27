# v = [4, 5, 5]
# a = 2
# b = 1

v = [4, 4, 3]
a = 2
b = 1

def solution(v, a, b):
    answer = 0

    while True:
        if min(v) < b or max(v) < a:
            break

        v.sort(reverse=True)

        v[0] -= a
        for i in range(1, len(v)):
            v[i] -= b

        answer += 1

    return answer

print(solution(v, a, b))