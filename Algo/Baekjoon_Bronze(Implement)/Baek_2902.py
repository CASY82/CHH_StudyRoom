import sys

word = sys.stdin.readline().strip()
wordList = word.split('-')
result = ''

for i in wordList:
    result += i[0]

print(result)