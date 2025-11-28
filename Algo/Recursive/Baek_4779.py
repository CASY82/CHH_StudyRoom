import sys

def make_cantor(n: int) -> str:
    length = 3 ** n
    arr = ['-'] * length

    def cantor(start: int, size: int):
        # 구간 길이가 1이면 더 쪼갤 수 없음
        if size == 1:
            return

        third = size // 3

        # 가운데 1/3 구간을 공백으로 채움
        for i in range(start + third, start + 2 * third):
            arr[i] = ' '

        # 왼쪽, 오른쪽 구간에 대해 재귀 호출
        cantor(start, third)
        cantor(start + 2 * third, third)

    cantor(0, length)
    return ''.join(arr)

out_lines = []

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue  # 빈 줄은 무시
    n = int(line)
    out_lines.append(make_cantor(n))

    # 한 번에 출력 (속도 조금 더 유리)
sys.stdout.write('\n'.join(out_lines))