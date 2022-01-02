import sys

word = sys.stdin.readline().strip()
count = "a,e,i,o,u".split(',')
result = 0

for i in count:
    result += word.count(i)

print(result)