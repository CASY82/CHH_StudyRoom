import sys

word = sys.stdin.readline().strip()

length = len(word)
answer = None

for i in range(1, length - 1):
    for j in range(i + 1, length):
        a = word[:i][::-1]
        b = word[i:j][::-1]
        c = word[j:][::-1]

        new_word = a + b + c

        if answer is None or new_word < answer:
            answer = new_word

print(answer)