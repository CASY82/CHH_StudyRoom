import sys

while True:
    data = list(sys.stdin.readline().strip().split())
    seat = int(data[0])

    if seat == 0:
        break

    customer = data[1]

    seats = set()
    fail_cnt = set()

    for i in range(len(customer)):
        if customer[i] not in seats:
            if len(seats) < seat:
                seats.add(customer[i])
            else:
                fail_cnt.add(customer[i])
        else:
            seats.discard(customer[i])

    if len(fail_cnt) == 0:
        print("All customers tanned successfully.")
    else:
        print("{} customer(s) walked away.".format(len(fail_cnt)))

# 다른 사람 풀이
# import sys
#
# try:
#     while True:
#         n, waiting = input().split()
#         goneCnt = 0
#         gone = set()
#         queue = []
#         n = int(n)
#         for cs in waiting:
#             if len(queue) < n and cs not in queue:
#                 queue.append(cs)
#             elif cs in queue:
#                 queue.remove(cs)
#             elif len(queue) == n and cs not in gone:
#                 gone.add(cs)
#                 goneCnt += 1
#         if goneCnt == 0:
#             print('All customers tanned successfully.')
#         else:
#             print(f'{goneCnt} customer(s) walked away.')
# except:
#     sys.exit(0)