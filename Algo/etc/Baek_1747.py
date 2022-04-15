import sys

n = int(sys.stdin.readline())

prime = [True] * 1003002
prime_num = []

for i in range(2, int(1003002 ** 0.5) + 1):
    if prime[i]:
        for j in range(i*i, 1003002, i):
            prime[j] = False

for i in range(2, 1003002):
    if prime[i]:
        prime_num.append(i)

prime_num.sort()

prime_palindrome = []

for i in prime_num:
    num_str = str(i)
    num_str_len = len(num_str)
    check = True
    for j in range(num_str_len//2):
        if num_str[j] != num_str[num_str_len-j-1]:
            check = False
            break

    if check:
        prime_palindrome.append(i)

for i in prime_palindrome:
    if i >= n:
        print(i)
        break