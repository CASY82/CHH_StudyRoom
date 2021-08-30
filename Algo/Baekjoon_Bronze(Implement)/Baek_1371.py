#긴 문장 입력 받는 방법
# sys read를 이용하는 방법
# import sys
# line = sys.stdin.read()
#
# #try except 이용하는 방법
# line = ''
# while True:
# 	try:
#     	line = input()
#    	except EOFError:
#     	break

alphabet_count = [0] * 26
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
max_alpha = []
sentense_list = []


while True:
    try:
        sentense = input()
        sentense_list.append(sentense)
    except EOFError:
        break

for i in sentense_list:
    for j in range(len(alphabet)):
        alphabet_count[j] += i.count(alphabet[j])

for i in range(len(alphabet_count)):
    if max(alphabet_count) == alphabet_count[i]:
        max_alpha.append(alphabet[i])

print("".join(max_alpha))