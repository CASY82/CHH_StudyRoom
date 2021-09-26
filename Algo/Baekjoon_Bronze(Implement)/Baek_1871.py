n = int(input())
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for _ in range(n):
    result = 0
    word, num = input().split('-')

    for i in range(3):
        for j in range(1, len(alpha)):
            if word[i] == alpha[j]:
                result += j * (26 ** (2 - i))

    if abs(result - int(num)) <= 100:
        print('nice')
    else:
        print('not nice')