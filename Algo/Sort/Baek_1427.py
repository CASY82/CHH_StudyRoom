#정렬을 이용한 문제.. 그러나 따로 알고리즘을 구현하여 풀진 않았다...
num = list(map(int, input()))
num.sort(reverse=True)

for i in num:
    print(i, sep='', end='')