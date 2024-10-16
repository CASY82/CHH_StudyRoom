import sys

n = int(sys.stdin.readline())
ptr = "ptr"
last_ptr = "a"

def pointer_func(next, ptr, last_ptr):
    if next > n:
        return

    next_ptr = "*" + ptr

    if next == 1:
        print("int {0} = &{1};".format(next_ptr, last_ptr))
        last_ptr = "ptr"
    else:
        print("int {0}{1} = &{2};".format(next_ptr, next, last_ptr))
        last_ptr = "ptr" + str(next)

    pointer_func(next + 1, next_ptr, last_ptr)


print("int a;")
pointer_func(1, ptr, last_ptr)

# 다른 사람 풀이
# def point_study(N):
#     print("int a;")
#
#     for idx in range(1, N + 1):
#         before_and_string = f"ptr{idx - 1 if idx - 1 > 1 else ''};" if idx > 1 else "a;"
#         print(f"int {'*' * idx}ptr{idx if idx > 1 else ''} = &{before_and_string}")
#
#
# if __name__ == "__main__":
#     N = int(input())
#     point_study(N=N)