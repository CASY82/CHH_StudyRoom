import sys

login = sys.stdin.readline().strip()

if login[:2] == "io" and login[2:].isdigit():
    print("Correct")
else:
    print("Incorrect")