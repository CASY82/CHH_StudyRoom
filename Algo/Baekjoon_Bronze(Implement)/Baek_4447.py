n = int(input())

for _ in range(n):
    name = input()
    nameTmp = name.lower()
    result = ''

    bCnt = nameTmp.count('b')
    gCnt = nameTmp.count('g')

    if bCnt > gCnt:
        result = 'A BADDY'
    elif bCnt < gCnt:
        result = 'GOOD'
    else:
        result = 'NEUTRAL'

    print(name, ' is ', result, sep='')