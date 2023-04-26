import sys

n = int(sys.stdin.readline())
words = []
shortCut = set()

for _ in range(n):
    word = list(sys.stdin.readline().strip().split())
    check = True

    for nb in range(len(word)):
        if word[nb][0].lower() not in shortCut:
            shortCut.add(word[nb][0].lower())
            word[nb] = "[" + word[nb][0] + "]" + word[nb][1:]
            check = False
            break

    word = " ".join(word)

    if check:
        for nb in range(len(word)):
            if word[nb] == " ":
                continue

            if word[nb].lower() not in shortCut:
                shortCut.add(word[nb].lower())
                word = word[:nb] + "[" + word[nb] + "]" + word[nb+1:]
                break

    words.append(word)

for result in words:
    print(result)

# 다른 사람 풀이 참고
# def c(x,i):
#  f=x[i].upper()not in s and b[0]
#  if f:s.add(x[i].upper());b[0]=0;x[i]='['+x[i]+']'
#  return f
# s=set()
# for _ in[0]*int(input()):
#  l=[[*x]for x in input().split()];b=[1]
#  for e in l:
#   if c(e,0):break
#  [c(e,i)for e in l for i in range(len(e))]
#  print(*[''.join(e)for e in l])