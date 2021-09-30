p, w = map(int, input().split())
word_list = list(input())

alpha = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alpha_time = [1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4]
alpha_location = [1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]
time_sum = 0
checker = 0
check = False

for i in range(len(word_list)):
    time_sum += alpha_time[alpha.index(word_list[i])] * p

    if checker == alpha_location[alpha.index(word_list[i])]:
        check = True
        checker = alpha_location[alpha.index(word_list[i])]
    else:
        check = False
        checker = alpha_location[alpha.index(word_list[i])]

    if check == True and word_list[i] != ' ':
        time_sum += w


print(time_sum)