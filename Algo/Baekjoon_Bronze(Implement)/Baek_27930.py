import sys

word = sys.stdin.readline().strip()
korea = "KOREA"
yonsei = "YONSEI"

k_index = 0
y_index = 0

for char in range(len(word)):
    if k_index < len(korea) and word[char] == korea[k_index]:
        k_index += 1
    if y_index < len(yonsei) and word[char] == yonsei[y_index]:
        y_index += 1

    # 두 학교 중 하나가 완성되면 출력
    if k_index == len(korea):
        print("KOREA")
        break
    if y_index == len(yonsei):
        print("YONSEI")
        break