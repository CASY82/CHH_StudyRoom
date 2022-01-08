#한두번 시뮬해보니 짝수일때는 무조건 창영이가 이기고, 홀수일 땐 상근이가 이김
import sys

if(int(sys.stdin.readline()) % 2 == 0):
    print("CY")
else:
    print("SK")