import re

# new_id = "...!@BaT#*..y.abcdefghijklm"
new_id = '=.='

def solution(new_id):
    answer = ''
    checker = '~!@#$%^&*()=+[{]}:?,<>/'

    if new_id != '':
        # 1단계
        new_id = new_id.lower()

        # 2단계
        new_id = ''.join(x for x in new_id if x not in checker)

        # 3단계 -- 이 부분만 참고...
        while True:
            new_id = new_id.replace('..', '.')

            if '..' not in new_id:
                break

        # 4단계
        if len(new_id) > 0 and new_id[0] == '.':
            new_id = new_id[1:]

        if len(new_id) > 0 and new_id[len(new_id) - 1] == '.':
            new_id = new_id[:-1]

    # 5단계
    if new_id == '':
        new_id = new_id + 'a'

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]

    # 7단계
    while len(new_id) < 3:
        if len(new_id) <= 2:
            new_id = new_id + new_id[len(new_id) - 1]

    if len(new_id) > 0 and new_id[0] == '.':
        new_id = new_id[1:]

    if len(new_id) > 0 and new_id[len(new_id) - 1] == '.':
        new_id = new_id[:-1]


    answer = new_id

    return answer


print(solution(new_id))