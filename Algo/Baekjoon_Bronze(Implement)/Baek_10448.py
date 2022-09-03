import sys

t_num = []
for i in range(1, 45):
    t_num.append((i*(i+1))//2)

n = int(sys.stdin.readline())
length = len(t_num)

for _ in range(n):
    num = int(sys.stdin.readline())
    tmp = False

    for i in range(length):
        for j in range(length):
            for k in range(length):
                if t_num[i] + t_num[j] + t_num[k] == num:
                    tmp = True
                    print(1)
                    break
            if tmp:
                break
        if tmp:
            break

    if not tmp:
        print(0)