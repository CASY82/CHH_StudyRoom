# <list>.sort()
# <list>.sort(key = <function>, reverse = True|Flase)
#
# sort함수는 원본의 내용을 정렬한 형태로 바꿔준다.
# key를 통해 정렬할 기준을 설정할 수 있다.
# reverse를 통해 오름차순, 내림차순을 결정할 수 있다 (True: 오름차순)
# list만 사용할 수 있다
# <newList> = sorted(<list>)
# <newList> = sorted(<list>, key = <function>, reverse = True|Flase)
#
# sorted함수는 원본의 내용을 바꾸지 않고 정렬된 내용을 반환해준다.
# 따라서 sorted함수를 사용해도 list의 내용은 변하지 않는다.
# list만 쓸 수 있는 sort함수와 달리 tuple, dictionary, str 같은 iterable객체라면 모두 사용 가능하다.
# 처리 속도는 sort보다 느리다.
# iterable객체 관련 내용
#
# 이중리스트 정렬
# arr = [[0, 'ji'], [1, 'won'], [2, 'han']]
# 의 형태를 가진 리스트의 경우
# arr[][0] 즉 숫자를 기준으로 정렬하고자 할 때는
# arr.sort(key=lambda x: x[0])
#
# arr[][1] 즉 문자열을 기준으로 정렬하고자 할 때는
# arr.sort(key=lambda x: x[1])
#
# 첫번째 인자를 기준으로 오름차순 정렬 후 두번째 인자를 기준으로 내림차순 정렬할 때
# arr.sort(key=lambda x: (x[0], -x[1]))
#
# 문자열의 길이를 기준으로 정렬
# arr.sort(key=lambda x: len(x))