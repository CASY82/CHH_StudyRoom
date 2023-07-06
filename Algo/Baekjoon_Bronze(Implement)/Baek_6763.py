import sys

cut = int(sys.stdin.readline())
speed = int(sys.stdin.readline())

fee = 0

if 1 <= speed-cut <= 20:
    fee = 100
elif 21 <= speed-cut <= 30:
    fee = 270
elif 31 <= speed-cut:
    fee = 500

if fee == 0:
    print("Congratulations, you are within the speed limit!")
else:
    print("You are speeding and your fine is ${}.".format(fee))