import sys

antena = int(sys.stdin.readline())
eyes = int(sys.stdin.readline())

if antena >= 3 and eyes <= 4:
    print("TroyMartian")
if antena <= 6 and eyes >= 2:
    print("VladSaturnian")
if antena <= 2 and eyes <= 3:
    print("GraemeMercurian")