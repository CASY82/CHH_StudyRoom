import sys

t = int(sys.stdin.readline())

for case in range(t):
    n = int(sys.stdin.readline())
    book = list(map(int, sys.stdin.readline().split()))

    odd_check = [True for _ in range(len(book))]
    odd = []
    even = []
    result = []

    for i in range(len(book)):
        if book[i] % 2 == 0:
            odd_check[i] = False
            even.append(book[i])
        else:
            odd.append(book[i])

    odd.sort()
    even.sort(reverse=True)

    odd_idx = 0
    even_idx = 0

    for j in range(len(book)):
        if odd_check[j]:
            result.append(odd[odd_idx])
            odd_idx += 1
        else:
            result.append(even[even_idx])
            even_idx += 1

    print("Case #{}:".format(case+1), *result)