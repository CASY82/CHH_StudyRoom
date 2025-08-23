import sys

while True:
    n = int(sys.stdin.readline())

    fir_queue = []
    sec_queue = []

    if n == 0:
        break

    if n % 2 == 1:
        for _ in range(n // 2 + 1):
            fir_queue.append(sys.stdin.readline().strip())

        for _ in range(n // 2):
            sec_queue.append(sys.stdin.readline().strip())

        for i in range(n // 2):
            print(fir_queue[i])
            print(sec_queue[i])

        print(fir_queue[-1])
    else:
        for _ in range(n // 2):
            fir_queue.append(sys.stdin.readline().strip())

        for _ in range(n // 2):
            sec_queue.append(sys.stdin.readline().strip())

        for i in range(n // 2):
            print(fir_queue[i])
            print(sec_queue[i])