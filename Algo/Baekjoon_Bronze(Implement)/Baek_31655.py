import sys

date = sys.stdin.readline().strip().split("/")

if int(date[0]) <= 12 and int(date[1]) <= 12:
    print("either")
elif int(date[0]) > 12:
    print("EU")
elif int(date[1]) > 12:
    print("US")