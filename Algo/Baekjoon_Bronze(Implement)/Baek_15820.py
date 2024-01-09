import sys

s1, s2 = map(int, sys.stdin.readline().split())
check = True

# 샘플 테스트
for _ in range(s1):
    q, a = map(int, sys.stdin.readline().split())

    if q != a:
        check = False
        break

if check:
    # 시스템 테스트
    for _ in range(s2):
        q, a = map(int, sys.stdin.readline().split())

        if q != a:
            print("Why Wrong!!!")
            check = False
            break

    if check:
        print("Accepted")
else:
    print("Wrong Answer")