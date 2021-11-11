#사실은 오름차순 배열 하나와 내림차순 배열 하나 총 두개의 배열 선언한 뒤 입력받은 배열과 비교한다음 두 경우와 모두 다르면 mixed 출력하면되긴한다... ㅋㅋ

num = list(map(int, input().split()))
check = []
state = ''

for i in range(1, len(num)):
    if num[i] > num[i-1]:
        check.append('ascending')
    else:
        check.append('descending')

first = check[0]
for j in check:
    if first == j:
        state = j
        continue
    else:
        state = 'mixed'
        break

print(state)