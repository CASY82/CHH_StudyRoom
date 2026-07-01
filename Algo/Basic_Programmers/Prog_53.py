# 코드 처리하기

def solution(num_list):
    odd = ""
    even = ""

    for i in num_list:
        if i % 2 == 1:
            odd = odd + str(i)
        else:
            even = even + str(i)

    answer = int(odd) + int(even)

    return answer

print(solution([3, 4, 5, 2, 1]))
print(solution([5, 7, 8, 3]))