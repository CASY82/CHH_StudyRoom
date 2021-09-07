n, m = map(int, input().split())
box_size = list(map(int, input().split()))
book_size = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        if box_size[i] >= book_size[j]:
            box_size[i] -= book_size[j]
            book_size[j] = 1001


print(sum(box_size))

#아닛...? 아... 문제의 조건에서 책을 하나라도 넣지 못하는 경우는 없다고 했다...
# n, m = map(int, input().split())
# box = list(map(int, input().split()))
# book = list(map(int, input().split()))
#
# print(sum(box) - sum(book))