# import sys
#
# n = int(sys.stdin.readline())
#
# for _ in range(n):
#     setense = []
#     result = 0
#
#     while True:
#         inputSentense = sys.stdin.readline().strip()
#
#         if inputSentense == "":
#             break
#
#         setense.append(inputSentense)
#
#     resultSentense = "".join(setense)
#
#     if len(resultSentense) != 0:
#         result = (len(resultSentense) - resultSentense.count("#")) * 100 / len(resultSentense)
#
#     if round(result, 1) % 1 == 0:
#         print("Efficiency ratio is ", int(result), "%.", sep="")
#     else:
#         print("Efficiency ratio is %.1f%%." % round(result, 1))

# 아직도 내 소스랑 뭐가 차이인지 알수 없어서 pass 아래는 참고 소스
N = int(input())

for i in range(N):
    tmp = [0, 0]
    while True:
        S = input()
        if S == "":
            break
        else:
            tmp[0] += len(S)
            tmp[1] += len(S) - S.count('#')
    sum = round(100 * tmp[1] / tmp[0], 1)

    if sum % 1 == 0:
        print("Efficiency ratio is %d%%." % int(sum))
    else:
        print("Efficiency ratio is %.1f%%." % sum)