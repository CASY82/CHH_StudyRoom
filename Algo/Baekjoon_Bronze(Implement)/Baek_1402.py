#너무 복잡하게 생각한 문제...
#이 문제는 결국 모든 A는 A'를 만들수 있기때문에 바로 yes를 출력하면된다.
#만들수 있는 이유는 A = A * 1 * 1 * 1....
#작은 수도 -1을 짝수번 곱해서 만들면 된다....

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    print('yes')
