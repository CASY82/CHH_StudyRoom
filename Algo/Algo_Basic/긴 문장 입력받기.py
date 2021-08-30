# sys read를 이용하는 방법
import sys
line = sys.stdin.read()

# #try except 이용하는 방법
line = ''
while True:
	try:
    	line = input()
   	except EOFError:
    	break