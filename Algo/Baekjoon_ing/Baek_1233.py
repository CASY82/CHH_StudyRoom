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
