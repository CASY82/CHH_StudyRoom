# 음.. 혼자 해보려했으나 실패. 굉장히 좋은 풀이가 있어 참고하였다.
import sys
sys.setrecursionlimit(10 ** 6)

def star(n):
    if n == 1:
        return ['*']

    Stars = star(n//3)
    array = []

    for s in Stars:
        array.append(s*3)
    for s in Stars:
        array.append(s + ' '*(n//3) + s)
    for s in Stars:
        array.append(s*3)

    return array

n = int(sys.stdin.readline().strip())
print('\n'.join(star(n)))