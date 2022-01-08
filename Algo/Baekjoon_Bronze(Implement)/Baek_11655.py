word = input()
ROT = ''

# print(ord('A')) 65
# print(ord('a')) 97
# print(ord('Z')) 90
# print(ord('z')) 122
for i in range(len(word)):
    if 65 <= ord(word[i]) <= 90:
        if ord(word[i]) + 13 > 90:
            ROT += chr((ord(word[i]) + 13) - 90 + 64)
        else:
            ROT += chr((ord(word[i]) + 13))
    elif 97 <= ord(word[i]) <= 122:
        if ord(word[i]) + 13 > 122:
            ROT += chr((ord(word[i]) + 13) - 122 + 96)
        else:
            ROT += chr((ord(word[i]) + 13))
    else:
        ROT += word[i]

print(ROT)