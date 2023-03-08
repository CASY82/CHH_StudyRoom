import sys

t = int(sys.stdin.readline())

for _ in range(t):
    num1 = sys.stdin.readline().strip()
    num2 = sys.stdin.readline().strip()

    cnt = 0

    for alpa in range(len(num1)):
        if num1[alpa] != num2[alpa]:
            cnt += 1

    print('Hamming distance is {}.'.format(cnt))