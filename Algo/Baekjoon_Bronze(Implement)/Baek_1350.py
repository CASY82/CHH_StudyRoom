n = int(input())
file_size = list(map(int, input().split()))
cluster_size = int(input())

result = 0

for i in range(n):
    if file_size[i] > cluster_size:
        if (file_size[i] % cluster_size) != 0:
            need_clu = (file_size[i] // cluster_size) + 1
        else:
            need_clu = (file_size[i] // cluster_size)
        result += cluster_size * need_clu
    elif file_size[i] == 0:
        continue
    else:
        result += cluster_size

print(result)