import sys

vowels = "a,e,i,o,u".split(",")
result = 0
n = int(sys.stdin.readline())
word = sys.stdin.readline().strip()

for vowel in vowels:
    result += word.count(vowel)

print(result)