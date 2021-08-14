sentense = ''
vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    result = 0
    sentense = input()
    sentense = sentense.lower()

    if sentense == '#':
        break

    for i in vowel:
        result += sentense.count(i)

    print(result)