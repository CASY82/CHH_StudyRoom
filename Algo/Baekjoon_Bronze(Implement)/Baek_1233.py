#결국은 답을 보고 풀게 되었다.... 정말 간단한건데 왜 생각이 안날까...
import time
start = time.time()
S1, S2, S3 = map(int, input().split())

result = [0] * 81

for i in range(1, S1 + 1):
    for j in range(1, S2 + 1):
        for k in range(1, S3 + 1):
            result[i + j + k] += 1


print(result.index(max(result)))
print("time : ", time.time() - start)

#딕셔너리 활용 방법
#
# s1, s2, s3 = map(int, input().split())
# d = {}
# for i in range(1, s1+1):
#     for j in range(1, s2+1):
#         for k in range(1, s3+1):
#             d[i+j+k] = d.get(i+j+k, 0) + 1
# li = sorted(d.items(), key=lambda x:x[0])
# li = sorted(li, key=lambda x:x[1], reverse=True)
# print(li[0][0])