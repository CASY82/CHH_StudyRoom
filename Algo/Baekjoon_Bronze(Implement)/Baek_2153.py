word = list(input())
sum = 0
check = False

alpha = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(len(word)):
    sum += alpha.index(word[i])

for j in range(2, sum):
    if sum % j == 0:
        check = True
        break

if check == True:
    print('It is not a prime word.')
else:
    print('It is a prime word.')
