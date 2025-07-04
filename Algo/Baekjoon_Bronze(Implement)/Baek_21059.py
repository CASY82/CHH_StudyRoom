import sys
sys.setrecursionlimit(500000)

# 페아노 공리에 따른 덧셈 함수 (내부 계산용)
# 이 함수는 변경할 필요가 없습니다.
def add(x, y):
    """
    페아노 공리를 사용하여 두 자연수를 더합니다. (내부 표현 사용)
    x + 0 = x
    x + S(y) = S(x + y)
    """
    if y == '0':
        return x
    else:
        y_prime = y[1]
        return ('S', add(x, y_prime))


# 페아노 공리에 따른 곱셈 함수 (내부 계산용)
# 이 함수는 변경할 필요가 없습니다.
def multiply(x, y):
    """
    페아노 공리를 사용하여 두 자연수를 곱합니다. (내부 표현 사용)
    x * 0 = 0
    x * S(y) = (x * y) + x
    """
    if y == '0':
        return '0'
    else:
        y_prime = y[1]
        recursive_result = multiply(x, y_prime)
        return add(recursive_result, x)


# --- 입출력 형식 변환을 위한 보조 함수 ---

def to_peano_internal(n):
    """정수 n을 프로그램 내부의 페아노 표현 ('S', ('S', '0'))으로 변환합니다."""
    if n == 0:
        return '0'
    else:
        return ('S', to_peano_internal(n - 1))


def from_peano_internal(p):
    """프로그램 내부의 페아노 표현 p를 정수로 변환합니다."""
    if p == '0':
        return 0
    else:
        # p[0]은 'S', p[1]은 그 안의 숫자 표현입니다.
        return 1 + from_peano_internal(p[1])


# --- 메인 실행 로직 ---

def solve():
    """
    두 줄의 페아노 수 문자열을 입력받아 그 곱을 페아노 수 문자열로 출력합니다.
    """
    # 1. 두 줄의 문자열 입력받기
    # sys.stdin.readline()은 개행문자(\n)를 포함하므로 .strip()으로 제거합니다.
    peano_str1 = sys.stdin.readline().strip()
    peano_str2 = sys.stdin.readline().strip()

    # 2. 입력 문자열을 정수로 변환 (S의 개수 세기)
    num1 = peano_str1.count('S')
    num2 = peano_str2.count('S')

    # 3. 정수를 내부 페아노 표현(튜플)으로 변환
    peano_internal1 = to_peano_internal(num1)
    peano_internal2 = to_peano_internal(num2)

    # 4. 곱셈 수행
    product_internal = multiply(peano_internal1, peano_internal2)

    # 5. 계산 결과를 다시 정수로 변환
    product_num = from_peano_internal(product_internal)

    # 6. 최종 정수 결과를 출력 형식에 맞는 문자열로 변환
    if product_num == 0:
        output_str = "0"
    else:
        # S( ... 0 ... ) 형식으로 만듭니다.
        # 'S('를 숫자만큼 반복하고, '0'을 붙이고, ')'를 숫자만큼 반복합니다.
        output_str = 'S(' * product_num + '0' + ')' * product_num

    # 7. 최종 결과 출력
    print(output_str)


# 프로그램 실행
solve()