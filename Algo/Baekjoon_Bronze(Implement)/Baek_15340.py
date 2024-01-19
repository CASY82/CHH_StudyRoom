import sys

while True:
    call, using_data = map(int, sys.stdin.readline().split())

    if call == using_data == 0:
        break

    # 파스텔
    pastel = call * 30 + using_data * 40
    # 파셀
    pasel = call * 35 + using_data * 30
    # 파스폰
    paspon = call * 40 + using_data * 20

    print(min(paspon, pasel, pastel))