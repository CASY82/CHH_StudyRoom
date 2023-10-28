import sys

word, period = sys.stdin.readline().strip().split()

word = word.lower()
period = int(period)
history = set()

start_check = word[0]
cnt = 1
result = ''

for i in range(1, len(word)):
    if start_check == word[i]:
       cnt += 1
    else:
        if start_check not in history:
            if cnt >= period:
                result += '1'
            else:
                result += '0'

            history.add(start_check)

        start_check = word[i]
        cnt = 1

#마지막 문자열 처리
if start_check not in history:
    if cnt >= period:
        result += '1'
    else:
        result += '0'

print(result)