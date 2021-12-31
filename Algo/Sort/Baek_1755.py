import sys

number = "zero,one,two,three,four,five,six,seven,eight,nine".split(',')
m, n = map(int, sys.stdin.readline().split())

numList = []

for i in range(m, n+1):
    # 수를 문자로 변환한다.
    word = ''
    tmp = list(map(str, str(i)))
    for j in range(len(tmp)):
        word += number[int(tmp[j])] + " "

    numList.append([word, i])

numList.sort(key = lambda x : x[0])

cnt = 0
for i,v in numList:
    if cnt == 10:
        print()
        print(v, end=' ')
        cnt = 1
    else:
        print(v, end=' ')
        cnt += 1