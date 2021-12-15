import sys
sipgan = [i for i in range(10)]
sipizi = list('A,B,C,D,E,F,G,H,I,J,K,L'.split(','))

n = int(sys.stdin.readline())

print(sipizi[(n-4)%12]+str(sipgan[(n+6)%10]))