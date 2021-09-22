# python3로 하면 시간 초과 pypy3로 하면 통과
n, c = map(int, input().split())
firecracker_time = [False] * (c + 1)

for i in range(n):
    student = int(input())

    for j in range(0, c + 1, student):
        if j % student == 0:
            firecracker_time[j] = True

print(firecracker_time.count(True) - 1) #굳이 count를 쓸필요없이 위 for문에서 개수를 세면 되지 않았나.. 그럼 시간이 줄어들어서 python으로도 가능했을거 같다.

#python 풀이 참고
# n,c = map(int,input().split(' '))
# cnt=0
# d = [0]*(c+1)
# for i in range(n):
#     a=int(input())
#     b=a
#     if a==1:
#         print(c)
#         cnt=0
#         break
#     while a<=c:
#         if d[a] == 0 :
#             cnt+=1
#             d[a]=1
#         a+=b
# if cnt != 0:
#     print(cnt)