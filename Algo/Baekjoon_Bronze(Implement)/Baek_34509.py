# 2, 4, 6, 8

# n은 두자리 수
for i in range(10, 100):
    if "8" not in str(i):
        tmp = int(str(i)[::-1])
        if tmp % 4 == 0:
            if (tmp % 10 + tmp // 10) % 6 == 0:
                print(i)