#손쉽게 푼 문제 다행이 앞에 무의미한 '0'을 붙이는 조건이 없어서 매우 쉽게 해결했다.
palindrome = ''

while True:
    palindrome = input()

    if palindrome == '0':
        break

    if palindrome == palindrome[::-1]:
        print('yes')
    else:
        print('no')