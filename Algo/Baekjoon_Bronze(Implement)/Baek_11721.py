import sys

word = sys.stdin.readline().strip()

for i in range((len(word)//10)+1):
    print(word[i*10:(i*10+10)])