import sys

while True:
    parity = sys.stdin.readline().strip()
    tmp = list(parity)
    last = tmp[-1]

    if parity == "#":
        break

    one_cnt = parity.count("1")

    tmp.pop()

    if last == "e" and one_cnt % 2 == 0:
        tmp.append("0")
    elif last == "e" and one_cnt % 2 == 1:
        tmp.append("1")
    elif last == "o" and one_cnt % 2 == 0:
        tmp.append("1")
    else:
        tmp.append("0")

    print("".join(tmp))