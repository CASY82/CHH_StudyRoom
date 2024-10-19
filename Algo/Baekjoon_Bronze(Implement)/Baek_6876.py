import sys
import string

t = int(sys.stdin.readline())

key = [[], [], ["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"], ["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R", "S"], ["T", "U", "V"], ["W", "X", "Y", "Z"]]
alpha = list(string.ascii_uppercase)

for _ in range(t):
    phone_num = sys.stdin.readline().strip()

    answer = ""

    for i in range(len(phone_num)):
        if phone_num[i] in alpha:
            for j in range(len(key)):
                if phone_num[i] in key[j]:
                    answer += str(j)
        elif phone_num[i] != "-":
            answer += phone_num[i]

    answer = answer[:3] + "-" + answer[3:6] + "-" + answer[6:10]

    print(answer)