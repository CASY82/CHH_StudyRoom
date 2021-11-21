#참고하여 푼 코드인데... 왜 b를..?
a, b, v = map(int, input().split())

result = (v - b) // (a - b)

if (v - b) % (a - b) > 0:
    result += 1

print(result)


# 두번째 다시 도전한 틀린 코드
# a, b, v = map(int, input().split())
#
# if a >= v:
#     print(1)
# else:
#     if v%(a-b) == 0:
#         print(v // (a - b) + 1 - (a//(a-b)))
#     else:
#         print(v // (a-b) + 1)

# 완전 처음에는 아래와 비슷하게 풀었었으나.. 몇개의 반례로 인해 틀렸는데.. 어떤 부분이 달랐던걸까...(아래 코드는 참고)
# a,b,v=map(int,input().split())
# print(1-(v-a)//(b-a))

#제일 처음 도전했을 때 내 풀이
# a,b,v=map(int,input().split())
# print(1+(v-a)//(a-b)) #==> 위 풀이와 다른 반례가 무엇일까....

#위 문제 반례
#9 1 1000000000