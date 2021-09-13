#함수로 빼서 하면 좀 더 깔끔해질거 같은데 귀찮다
destination, source = map(int, input().split())

if source % 4 == 0:
    source_index_col = (source // 4) - 1
    source_index_row = 4
else:
    source_index_col = (source // 4)
    source_index_row = source % 4

if destination % 4 == 0:
    destination_index_col = (destination // 4) - 1
    destination_index_row = 4
else:
    destination_index_col = (destination // 4)
    destination_index_row = destination % 4

result = abs(source_index_col - destination_index_col) + abs(source_index_row - destination_index_row)

print(result)

# for i in range(source):
#     num_list.append([start_num + i for i in range(4)])
#     start_num += 4
