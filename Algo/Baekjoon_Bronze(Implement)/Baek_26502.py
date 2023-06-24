import sys

origin = "a e i o u y A E I O U Y".split()
replacement = "y a e i o u Y A E I O U".split()

n = int(sys.stdin.readline())

for _ in range(n):
    sentence = sys.stdin.readline().strip()
    result = ''

    for i in range(len(sentence)):
        if sentence[i] in origin:
            result += origin[replacement.index(sentence[i])]
        else:
            result += sentence[i]

    print(result)