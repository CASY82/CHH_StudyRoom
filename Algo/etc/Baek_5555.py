import sys

word = input()
n = int(sys.stdin.readline())
cnt = 0

for _ in range(n):
    compare_word = input()
    length = len(compare_word)

    #편법을 써서 맨 뒤에 word의 길이만큼 compare_word의 앞부분을 compare_word뒤에 붙인다. 그리고 나서 기존 compare_word의 길이까지만 word와 동일하면 +1
    compare_word += compare_word[:len(word)]

    find = 0
    if length < len(word):
        continue
    else:
        while find < length:
            check = False
            if compare_word[find] == word[0]:
                for i in range(len(word)):
                    if compare_word[find + i] == word[i]:
                        check = True
                    else:
                        check = False
                        find += 1
                        break

            else:
                find += 1

            if check:
                cnt += 1
                break

print(cnt)

# ABCD
# 1
# ABCDXXXXXX

#아니 이 간단할걸 3번이나 틀려가며;;; 아직도 문자열을 너무 못다루는거 아닌가...?
# k = input()
# n = int(input())
# ans = 0
#
# for _ in range(n):
# 	s1 = input()
# 	s = s1 + s1[0:len(k)-1]
# 	for i in range(len(s)):
# 		if k==s[i:i+len(k)]:
# 			ans += 1
# 			break
#
# print(ans)