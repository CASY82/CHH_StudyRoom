import sys

t = int(sys.stdin.readline())

tmp = "0 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ")

for _ in range(t):
    cnt, problem = sys.stdin.readline().split()

    pro_list = list(sys.stdin.readline().split())

    if problem == "C":
        for alpha in pro_list:
            print(tmp.index(alpha), end=" ")
    else:
        for num in pro_list:
            print(tmp[int(num)], end=" ")

    print()