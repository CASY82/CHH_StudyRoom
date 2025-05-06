# 철자 변환 규칙 (수정본 -> 원본)
rules = {
    '@': 'a',
    '[': 'c',
    '!': 'i',
    ';': 'j',
    '^': 'n',
    '0': 'o',
    '7': 't',
    '\\\'': 'v',  # \'
    '\\\\\'': 'w' # \\'
}

def process_word(word):
    alphabet_count = 0  # 원래 소문자 + 바뀐 문자
    changed_count = 0   # 바뀐 문자 개수
    original = []       # 복원된 단어
    i = 0               # 문자열 인덱스

    while i < len(word):
        # \\' (w) 패턴 확인 (3글자)
        if i + 2 < len(word) and word[i:i+3] == '\\\\\'':
            alphabet_count += 1
            changed_count += 1
            original.append('w')
            i += 3
        # \' (v) 패턴 확인 (2글자)
        elif i + 1 < len(word) and word[i:i+2] == '\\\'':
            alphabet_count += 1
            changed_count += 1
            original.append('v')
            i += 2
        # 단일 문자 확인
        else:
            char = word[i]
            # rules에 있는 단일 문자
            if char in rules:
                alphabet_count += 1
                changed_count += 1
                original.append(rules[char])
            # 소문자
            elif char.islower():
                alphabet_count += 1
                original.append(char)
            # 그 외 문자 (소문자도 바뀐 문자도 아님)
            else:
                original.append(char)
            i += 1

    # 바뀐 문자가 절반 초과인지 확인
    if alphabet_count > 0 and changed_count * 2 >= alphabet_count:
        return "I don't understand"
    else:
        return ''.join(original)

# 입력 처리
n = int(input())
for _ in range(n):
    word = input().strip()
    print(process_word(word))

# 다른 사람 풀이

# 백준 28125

# import io
#
# input = io.BufferedReader(io.FileIO(0), 1<<18).readline
#
#
# def solve(string):
#     changeStr = {"@", "[", "!", ";", "^", "0", "7", "\\"}
#     change = {"@": 'a', "[": 'c', "!": 'i', ";": 'j', "^": 'n', \
#             "0": 'o', "7": 't', "\\'": 'v', "\\\\'": 'w'}
#
#     result = ""
#     index = 0
#     changeCount = 0
#     while index < len(string):
#         if string[index] in changeStr:
#             if string[index] == '\\':
#                 if string[index+1] == "'":
#                     result += change["\\'"]
#                     index += 1
#                 elif string[index+1] == '\\' and string[index+2] == "'":
#                     result += change["\\\\'"]
#                     index += 2
#             else:
#                 if string[index] in changeStr:
#                     result += change[string[index]]
#             changeCount += 1
#         else:
#             result += string[index]
#         index += 1
#
#     return "I don't understand" if changeCount*2 >= len(result) else result
#
#
# def main():
#     N = int(input())
#     for _ in range(N):
#         string = input().decode().rstrip()
#         print(solve(string))
#
#
# main()
