import sys

word = sys.stdin.readline().strip()

a = word.count("A")
b = word.count("B")
c = word.count("C")

if a > 0:
    for char in ['B', 'C', 'D', 'F']:
        word = word.replace(char, 'A')
elif a == 0 and b > 0:
    for char in ['C', 'D', 'F']:
        word = word.replace(char, 'B')
elif a == 0 and b == 0 and c > 0:
    for char in ['D', 'F']:
        word = word.replace(char, 'C')
elif a == 0 and b == 0 and c == 0:
    tmp = ""
    for i in range(len(word)):
        tmp += "A"

    word = tmp

print(word)