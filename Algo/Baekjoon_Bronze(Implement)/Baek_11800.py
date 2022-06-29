import sys

t = int(sys.stdin.readline())

same_num = ["", "Habb Yakk", "Dobara", "Dousa", "Dorgy", "Dabash", "Dosh"]
num = ["", "Yakk", "Doh", "Seh", "Ghar", "Bang", "Sheesh"]

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())

    print("Case {}: ".format(i+1), end="")
    if a == b:
        print(same_num[a])
    else:
        if (a == 5 and b == 6) or (a == 6 and b == 5):
            print("Sheesh Beesh")
        else:
            print(num[max(a, b)], num[min(a, b)])