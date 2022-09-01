import sys

n, m = map(int, sys.stdin.readline().split())
need_boxes = 0

if n > 0:
    books = list(map(int, sys.stdin.readline().split()))

    while True:
        if sum(books) == n * (m+1):
            break

        tmp = 0

        for i in range(n):
            if books[i] != m + 1:
                if tmp + books[i] <= m:
                    tmp += books[i]
                    books[i] = m + 1
                else:
                    break

        need_boxes += 1

print(need_boxes)