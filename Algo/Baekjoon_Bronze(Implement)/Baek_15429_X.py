# import sys
#
# t = int(sys.stdin.readline())
#
# for _ in range(t):
#     gnome_array = list(map(int, sys.stdin.readline().split()))
#
#     for i in range(1, gnome_array[0]-1):
#         if gnome_array[i-1] <= gnome_array[i+1] and (gnome_array[i-1] >= gnome_array[i] or gnome_array[i] >= gnome_array[i+1]):
#             print(i+1)

# 다른 사람 풀이
import sys

for _ in range(int(input())):
    n = list(map(int, sys.stdin.readline().split()))[1:]

    index = 1

    for i in range(1, len(n)):
        index += 1

        if (n[i] - n[i - 1]) != 1:
            print(index)
            break