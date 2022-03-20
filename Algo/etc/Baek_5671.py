import sys

while True:
    try:
        n, m = map(int, sys.stdin.readline().split())
    except:
        break

    cnt = 0

    for room_num in range(n, m+1):
        check = True
        for i in range(10):
            if str(room_num).count(str(i)) > 1:
                check = False
                break

        if check:
            cnt += 1

    print(cnt)

# 다음 방법 괜찮다고 생각되어 가져와봄

# while True:
#     try: N, M = map(int, input().split())
#     except: break
#     count = 0
#     for i in range(N, M+1):
#         str_i = str(i)
#         remove_str_i = ''.join(set(str_i))   # set으로 판별하네!
#         if len(str_i) == len(remove_str_i): count += 1
#     print(count)