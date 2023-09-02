import sys

greetings = sys.stdin.readline().strip()

cnt = greetings.count("e")
cnt *= 2

result = ""
result += "h"

for _ in range(cnt):
    result += "e"

result += "y"

print(result)