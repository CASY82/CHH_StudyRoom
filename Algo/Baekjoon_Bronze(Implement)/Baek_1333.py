n, l, d = map(int, input().split())
time = 0
music_count = 0
bell_time = d
music_start = 0
music_end = music_start + l

while True:
    if time == music_end:
        music_start = music_end + 5
        if music_end <= bell_time and music_start > bell_time:
            print(bell_time)
            break
        else:
            music_count += 1
            music_end = music_start + l

    if time == bell_time:
        bell_time += d

    if music_count == n:
        print(bell_time)
        break

    time += 1

#다른 사람 풀이 참고(짧게 풀 수 있었던문제인거 같아서 참고해봤다)
# n,l,d=map(int,input().split())
# A=[0]*(n*(l+5)-5)
# for i in range(n):
#     s=(l+5)*i
#     for j in range(s,s+l):
#         A[j]=True
# r=0
# while r<len(A):
#     if not A[r]:
#         break
#     r+=d
# print(r)