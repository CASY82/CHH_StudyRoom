import sys

passing_word = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
word = sys.stdin.readline().strip().split()
result = ''

for i in range(len(word)):
    if i == 0 or word[i] not in passing_word:
        result += word[i][0].upper()

print(result)