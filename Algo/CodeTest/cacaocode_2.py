# 20210911 2  2 (절반 맞고 나머지 절반 실패 일단 pass)

n = 437674
k = 3

# n = 110011
# k = 10

def prime_check(num):
    if num == 2:
        return True

    for i in range(2, int(int(num) ** 0.5)):
        if num % i == 0:
            return False

        return True

def solution(n, k):
    answer = 0
    num = n
    k_num_list = []

    while True:
        k_num_list.append(str(num % k))
        num //= k

        if num <= 1:
            k_num_list.append(str(num % k))
            break

    k_num_list.reverse()
    change_num = ''.join(k_num_list)

    prime = []
    new_age = ''

    for i in range(len(change_num)):
        if change_num[i] == '0':
            if new_age != '':
                prime.append(new_age)
            new_age = ''
        else:
            new_age += change_num[i]

    prime.append(new_age)

    for i in range(len(prime)):
        if prime_check(int(prime[i])):
            answer += 1

    return answer

print(solution(n, k))