import sys

n = int(sys.stdin.readline())
word_list = list(sys.stdin.readline().strip() for _ in range(n))
cnt = 0

#마지막까지 돌 필요 없으므로
for i in range(n-1):
    #얘는 마지막까지 돌아야 하므로
    for j in range(i+1, n):
        word1 = word_list[i]
        word2 = word_list[j]

        flag = True
        checking1 = [0] * 26
        checking2 = [0] * 26

        # 단어 하나에 대해서 체킹
        for k in range(len(word1)):
            tmp1 = ord(word1[k]) - ord('a')
            tmp2 = ord(word2[k]) - ord('a')

            if checking1[tmp1] == 0 and checking2[tmp2] == 0:
                checking1[tmp1] = word2[k]
                checking2[tmp2] = word1[k]
            elif checking1[tmp1] != word2[k]:
                flag = False
                break

        if flag:
            cnt += 1

print(cnt)

# 참고 소스
# import sys
#
#
# n = int(sys.stdin.readline())
# temp = [[] for _ in range(101)]
# dic = [{} for i in range(101)]
# cnt = 0
#
# # 반복문을 통해 단어를 확인
# for i in range(n):
#     num = 0
#     m = str(sys.stdin.readline()).rstrip('\n')
#
#     # 반복문을 통해 알파벳을 확인하고
#     # 그 알파벳을 수와 같이 딕셔너리형으로 추가한다.
#     for j in m:
#         if j not in dic[i]:
#             dic[i][j] = str(num)
#             num += 1
#
#         # 현재 확인한 알파벳을 temp에 추가한다.
#         temp[i] += dic[i][j]
#
# 반복문을 통해 같은 단어라면 카운트한다.
# for i in range(n):
#     for j in range(i + 1, n):
#         if temp[i] == temp[j]:
#             cnt += 1
#
# print(cnt)