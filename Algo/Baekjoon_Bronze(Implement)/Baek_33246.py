import sys

n = int(sys.stdin.readline())
origin = sys.stdin.readline().strip()
check = True

for _ in range(n):
    check_word, status = sys.stdin.readline().strip().split()
    cnt = 0

    if len(check_word) == len(origin):
        for i in range(len(origin)):
            if check_word[i] != origin[i]:
                cnt += 1

            if cnt >= 2:
                break

        if cnt < 2:
            if status != "ALLOWED":
                check = False
                break
        else:
            if status != "DENIED":
                check = False
                break
    else:
        if status != "DENIED":
            check = False
            break

if check:
    print("SYSTEM SECURE")
else:
    print("INTEGRITY OVERFLOW")