n = int(input())
susic = []

for i in range((2 * n) - 1):
    word = input()
    if word == '/':
        word = '//'

    susic.append(word)

print(eval(''.join(susic)))
