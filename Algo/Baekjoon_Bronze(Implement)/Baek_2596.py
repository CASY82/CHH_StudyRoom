# A = '000000'
# B = '001111'
# C = '010011'
# D = '011100'
# E = '100110'
# F = '101001'
# G = '110101'
# H = '111010'

num_char = int(input())
char_list = input()

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
num_list = ['000000', '001111', '010011', '011100', '100110', '101001', '110101', '111010']
char_in_list = []
result = []
breaker = 0

for i in range(num_char):
    char_in_list.append(char_list[(i * 6):(i * 6) + 6])

for j in char_in_list:
    breaker += 1
    checker = False
    con = False
    for k in range(len(num_list)):
        if j == num_list[k]:
            result.append(alpha[num_list.index(num_list[k])])
            checker = True

    if checker == False:
        for k in range(8):
            checking_word = num_list[k]
            word_wrong = [0 for i in range(6)]
            for z in range(6):
                if checking_word[z] != j[z]:
                    word_wrong[z] += 1

            if sum(word_wrong) == 1:
                result.append(alpha[num_list.index(num_list[k])])
                con = True
            else:
                continue

        if con == False:
            breaker -= 1
            break

if breaker == num_char and result:
    print(''.join(result))
else:
    print(breaker+1)