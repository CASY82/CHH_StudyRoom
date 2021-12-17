number = "1924"
k = 2

number = "4177252841"
k = 4

def solution(number, k):
    answer = ''
    num_list = []

    for i, v in enumerate(number):
        while num_list and num_list[-1] < v and k > 0:
            num_list.pop()
            k -= 1

        if k == 0:
            num_list.extend([x for x in number[i:]])
            break

        num_list.append(v)

    num_list = (num_list[:-k] if k > 0 else num_list)

    answer = ''.join(num_list)

    return answer

print(solution(number, k))