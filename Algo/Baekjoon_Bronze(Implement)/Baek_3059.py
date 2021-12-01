#한번만 빼야되는건지 몰라서 한번 틀림;;
t = int(input())

for _ in range(t):
    word = input()
    ascii_sum = 2015
    sum_num = 0

    word = list(set(word))

    for i in word:
        sum_num += ord(i)

    print(ascii_sum - sum_num)