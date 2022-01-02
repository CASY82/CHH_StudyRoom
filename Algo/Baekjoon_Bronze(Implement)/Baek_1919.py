fir = input()
sec = input()
fir_count = []
sec_count = []
count = 0

fir_word = list(set(fir))
sec_word = list(set(sec))

fir_word.sort()
sec_word.sort()

for i in range(len(fir_word)):
    fir_count.append(sec.count(fir_word[i]))

for j in range(len(sec_word)):
    sec_count.append(fir.count(sec_word[j]))

for i in range(len(fir_word)):
    for j in range(len(sec_word)):
        if fir_word[i] == sec_word[j]:
            if fir_count[i] != sec_count[j]:
                count += min(fir_count[i], sec_count[j])
            else:
                count += fir_count[i]

print(len(fir) + len(sec) - 2 * count)

#음... 쉽게 푸는 법

# a = list(input())
# b = list(input())
# a_answer = 0
# for i in a:
#     if i in b:
#         b.remove(i)
#         a_answer += 1
# print(len(a) - a_answer + len(b))