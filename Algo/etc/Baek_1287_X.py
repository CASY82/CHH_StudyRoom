# import sys
#
# sick = sys.stdin.readline().strip()
# num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
# oper = ["+", "*", "-", "/"]
# check = True
#
# numCnt = 0
# operCnt = 0
#
# for i in range(len(num)):
#     numCnt += sick.count(num[i])
#
# for j in range(len(oper)):
#     operCnt += sick.count(oper[j])
#
# if numCnt - 1 == operCnt:
#     check = True
#
# for i in range(len(sick)-1):
#     if sick[i] in oper:
#         if i > 0 and sick[i - 1] in oper or sick[i + 1] in oper:
#             check = False
#             break
#
# print(check, operCnt, numCnt)
#
# try:
#     if check:
#         print(int(eval(sick)))
#     else:
#         print("ROCK")
# except:
#     print("ROCK")

# 다른 사람 소스 참고
# def rank(op):
#     if op == '(':
#         if flag==0:
#             return 20
#         else :
#             return 0
#     elif op == ')': return 19
#     elif op in '*/': return 15
#     elif op in '+-': return 14
#
# def calc(A,B,op):
#     if op=='+':
#         return A+B
#     elif op=='-':
#         return A-B
#     elif op=='*':
#         return A*B
#     elif op=='/':
#         sA=str(A)
#         sB=str(B)
#         if len(sA)-len(sB)>15:
#             real=A//B
#         return A//B
#
# flag=0
# input=input()#'1+(3-(+2+4))'#1*(2+3)
# origin=[]
# stackA=[]
# stackB=[]
# text=''
# op=1
# try:
#     for i in input:#토크나이저
#         if i in '+-*/()':
#             if text!='':#이걸로 ()의 예외 제어
#                 origin.append(int(text))
#             origin.append(i)
#             text=''
#         else :
#             text+=i
#     if text!='':
#         origin.append(int(text))
#     ###############################print(origin)
#     '''
#     5*(6*7+8)
#
#     5 6 7 * 8 + *
#
#     5 6 7 * 8
#     * ( +      )
# +(1+2+(2+3)
#     (5*6)+3
#     5 6 *
#     (      )
#     5 6 * 3 +
#     '''
#     for i in origin:
#         #print(i)
#         if op>=2 or op==-1 : print(10/0)
#         if type(i)==type(1):
#             op-=1
#             stackA.append(i)
#         else:
#
#             if i=='(':
#                 if op==0:print(10/0)
#                 stackB.append(i)
#                 flag+=1
#             elif i==')':
#                 if op==1:print(10/0)
#                 flag-=1
#                 #print(stackB)
#                 while stackB[len(stackB)-1]!='(':
#                     stackA.append(stackB.pop())
#                 stackB.pop()
#             elif len(stackB) <= 0:
#                 op+=1
#                 stackB.append(i)
#             else :
#                 op+=1
#                 if rank(stackB[len(stackB)-1])>=rank(i):
#                     stackA.append(stackB.pop())
#                     stackB.append(i)
#                 else:
#                     stackB.append(i)
#
#     del(origin)#메모리확보
#     '''
#     for i in origin:
#         #print(i)
#         if type(i)==type(1):
#             stackA.append(i)
#         else :
#             if len(stackB)<=0 :
#                 stackB.append(i)
#                 #print(i)
#             else:
#                 if rank(stackB[len(stackB)-1])>=rank(i):
#                     stackA.append(stackB.pop())
#                     stackB.append(i)
#                 else:
#                     stackB.append(i)
#     '''
#     #print(stackA)
#     #print(stackB)
#     while stackB:stackA.append(stackB.pop())
#     ##############################print(stackA)
#
#     for i in stackA:#stackB를 결과로 재활용
#         if type(i)==type(1):
#             stackB.append(i)
#         else:
#             B=stackB.pop()
#             A=stackB.pop()
#             stackB.append(calc(A,B,i))
#     del(stackA)
#     #print(9999999999999999999999999999999999999999999999999999999999999999999999999999999999/9)
#     print(stackB.pop())
#
# except:
#     print('ROCK')

# def rank(op):
#     if op == '(':
#         if flag==0:
#             return 20
#         else :
#             return 0
#     elif op == ')': return 19
#     elif op in '*/': return 15
#     elif op in '+-': return 14
#
# def calc(A,B,op):
#     if op=='+':
#         return A+B
#     elif op=='-':
#         return A-B
#     elif op=='*':
#         return A*B
#     elif op=='/':
#         sA=str(A)
#         sB=str(B)
#         if len(sA)-len(sB)>15:
#             real=A//B
#         return A//B
#
# flag=0
# input=input()#'1+(3-(+2+4))'#1*(2+3)
# origin=[]
# stackA=[]
# stackB=[]
# text=''
# op=1
# try:
#     for i in input:#토크나이저
#         if i in '+-*/()':
#             if text!='':#이걸로 ()의 예외 제어
#                 origin.append(int(text))
#             origin.append(i)
#             text=''
#         else :
#             text+=i
#     if text!='':
#         origin.append(int(text))
#
#     for i in origin:
#
#         if op>=2 or op==-1 : print(10/0)
#         if type(i)==type(1):
#             op-=1
#             stackA.append(i)
#         else:
#
#             if i=='(':
#                 if op==0:print(10/0)
#                 stackB.append(i)
#                 flag+=1
#             elif i==')':
#                 if op==1:print(10/0)
#                 flag-=1
#
#                 while stackB[len(stackB)-1]!='(':
#                     stackA.append(stackB.pop())
#                 stackB.pop()
#             elif len(stackB) <= 0:
#                 op+=1
#                 stackB.append(i)
#             else :
#                 op+=1
#                 if rank(stackB[len(stackB)-1])>=rank(i):
#                     stackA.append(stackB.pop())
#                     stackB.append(i)
#                 else:
#                     stackB.append(i)
#
#     del(origin)#메모리확보
#
#     while stackB:stackA.append(stackB.pop())
#
#     for i in stackA:#stackB를 결과로 재활용
#         if type(i)==type(1):
#             stackB.append(i)
#         else:
#             B=stackB.pop()
#             A=stackB.pop()
#             stackB.append(calc(A,B,i))
#     del(stackA)
#     print(stackB.pop())
#
# except:
#     print('ROCK')

# # 위는 정석적인 코드였고 날먹이 가능할거라고 생각했는데 다른 사람이 올려둔 코드가 있다;;;;(여기는 이제 안통함)
# import sys
#
# input = sys.stdin.readline
#
# ori = input()
# ori = ori.strip()
# if ori.find("()") != -1:
#     print("ROCK")
#     quit()
#
# rep = '&'
# # 아무래도 내가 생각하지 못했던것이 replace였던거 같다. 이걸 잘 활용했다면 쉽게 풀었을듯?
# # 해당 부분에서 연산자가 연속 되는 것을 걸러낸다.
# check = ori.replace('/', rep).replace('-', rep).replace('+', rep).replace('*', rep)
#
# try:
#     eval(check)
# except:
#     print("ROCK")
#     quit()
#
# try:
#     # 소수점을 어떻게 처리해야하나 고민했는데 너무 간단하게 처리되어서 놀람;;;
#     print(eval(ori.replace('/', "//")))
# except:
#     print("ROCK")


#이제 통하는 소스 날먹(?) 안됨
# import sys
#
# input = sys.stdin.readline
#
#
# def sol(Equation):
#     if Equation[0] in "+-/*" or Equation[-1] in "+-/*":
#         return "ROCK"
#     for i in range(len(Equation) - 1):
#         if Equation[i] in "+-/*(" and Equation[i + 1] in "+-/*)":
#             return "ROCK"
#
#     try:
#         return eval(Equation.replace("/", "//").replace("(" * 50, "").replace(")" * 50, ""))
#     except:
#         return "ROCK"
#
#
# print(sol(input().rstrip()))

import sys

sys.setrecursionlimit(50000000)

def evaluate_expression(expr):
    def parse_expression(tokens):
        def parse_primary():
            token = tokens.pop(0)
            if token == '(':
                value = parse_expression(tokens)
                tokens.pop(0)  # pop ')'
                return value
            return int(token)

        def parse_term():
            value = parse_primary()
            while tokens and tokens[0] in ('*', '/'):
                op = tokens.pop(0)
                if op == '*':
                    value *= parse_primary()
                elif op == '/':
                    divisor = parse_primary()
                    if divisor == 0:
                        raise ValueError("Division by zero")
                    value //= divisor
            return value

        value = parse_term()
        while tokens and tokens[0] in ('+', '-'):
            op = tokens.pop(0)
            if op == '+':
                value += parse_term()
            elif op == '-':
                value -= parse_term()
        return value

    def tokenize(expr):
        tokens = []
        num = ''
        for char in expr:
            if char.isdigit():
                num += char
            else:
                if num:
                    tokens.append(num)
                    num = ''
                if char in '+-*/()':
                    tokens.append(char)
        if num:
            tokens.append(num)
        return tokens

    # 토큰화
    tokens = tokenize(expr)

    try:
        result = parse_expression(tokens)  # tokens 인자를 전달
        if tokens:
            raise ValueError("Invalid expression")
        return result
    except (ValueError, IndexError):
        return "ROCK"

# 입력 받기
expression = input().strip()
print(evaluate_expression(expression))

# 다른 사람 풀이
# import sys
# sys.setrecursionlimit(2*10**5)
# class num(int):
#     def __init__(self,n):
#         self.n=int(n)
#     def __pos__(self):
#         raise
#     def __neg__(self):
#         raise
#     def __pow__(self,n):
#         raise
# s=input()
# l=[]
# f=1
# for i in s:
#     if i.isdigit():
#         if f:
#             l+='num("'
#         f=0
#     else:
#         if f<1:
#             l+='")'
#         f=1
#     l+=i
# if f==0:
#     l+='")'
# news=''.join(l)
# try:
#     n=int(eval(news.replace('/','//')))
#     print(n)
# except:
#     print('ROCK')

# 다른 사람 풀이2

# import sys
# input = sys.stdin.readline
#
# s = input().strip()
#
# if s[0] in '+-*/':
#     print('ROCK')
#     sys.exit()
# if s[-1] in '+-*/':
#     print('ROCK')
#     sys.exit()
#
# depth = 0
# prv = '+'
# value = []
# lz = True
# S = ''
# for j in range(len(s)):
#     i = s[j]
#     if i == '(':
#         if prv in ')0123456789':
#             print('ROCK')
#             sys.exit()
#         depth += 1
#         if S == '':
#             value.append('0+')
#         else:
#             value.append(S)
#         S = ''
#         prv = i
#         continue
#     if i == ')':
#         if prv in '(+-*/':
#             print('ROCK')
#             sys.exit()
#         depth -= 1
#         if depth < 0:
#             print('ROCK')
#             sys.exit()
#         try:
#             x = str(eval(S.replace('/', '//')))
#         except:
#             print('ROCK')
#             sys.exit()
#         S = value.pop() + x
#         prv = i
#         continue
#     if i in '+-*/':
#         if prv in '+-*/(':
#             print('ROCK')
#             sys.exit()
#     if i in '0123456789':
#         if prv != '0' and i != '0':
#             lz = False
#         if prv == ')':
#             print('ROCK')
#             sys.exit()
#     else:
#         lz = True
#
#     if not (i == '0' and j != len(s)-1 and s[j+1] in '0123456789' and lz):
#         S += i
#     prv = i
#
# if depth != 0:
#     print('ROCK')
#     sys.exit()
#
# try:
#     x = eval(S.replace('/', '//'))
# except:
#     print('ROCK')
#     sys.exit()
# print(x)