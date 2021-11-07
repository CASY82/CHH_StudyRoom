word = list(input())
cencor = list('CAMBRIDGE')
result = ''

for i in word:
    if not i in cencor:
        result += i

print(result)