import sys

n = int(sys.stdin.readline())

for i in range(n, -1, -1):
    if i == 0:
        if n != 1:
            print("No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, {} bottles of beer on the wall.".format(n))
        else:
            print("No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 1 bottle of beer on the wall.")
    elif i == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.")
    elif i == 2:
        print("2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.")
    else:
        print("{0} bottles of beer on the wall, {0} bottles of beer.\nTake one down and pass it around, {1} bottles of beer on the wall.".format(i, i-1))

    print()