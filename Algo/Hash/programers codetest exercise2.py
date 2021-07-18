# 해시 2 전화번호 목록

#["119", "97674223", "1195524421"]
#["123","456","789"]
#["12","123","1235","567","88"]
phone_num = ["12","123","1235","567","88"]

# 시간 초과가 난 코드... 반성 합시다
#
# def solution(phone_book):
#     answer = True
#     book_len = len(phone_book)
#     checker = ''
#
#     for i in range(book_len):
#         for j in range(book_len):
#             checker = phone_book[i]
#             if checker != phone_book[j] and phone_book[j].startswith(checker):
#                 answer = False
#                 break
#
#         if answer == False:
#             break
#
#     return answer



def solution(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True



print(solution(phone_num))