# 성공하긴 했지만 매우 지저분... Stack을 써서 풀어보았다.
word = list(input())

count = 0

while True:
    if len(word) == 0:
        break

    if word[len(word) - 1] == '=':
        if word[len(word) - 2] == 'z':
            if word[len(word) - 3] == 'd':
                for _ in range(3):
                    word.pop()
            else:
                for _ in range(2):
                    word.pop()
        else:
            for _ in range(2):
                word.pop()
    elif word[len(word) - 1] == '-':
        word.pop()
        word.pop()
    elif word[len(word) - 1] == 'j':
       if word[len(word) - 2] == 'l' or word[len(word) - 2] == 'n':
            word.pop()
            word.pop()
       else:
            word.pop()
    else:
        word.pop()

    count += 1

print(count)

#다른 사람 풀이 (더 짧게 나올 수 있게 할 수 있어서 참고해 보았다.)
# a = ['c=','c-','dz=','d-','lj','nj','s=','z=']
# alpha = input()
#
# for t in a:
#     alpha = alpha.replace(t, "*")
# print(len(alpha))