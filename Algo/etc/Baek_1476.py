import sys

e, s, m = map(int, sys.stdin.readline().split())
year = 1

while True:
    e_result = year % 15
    if e_result == 0:
        e_result = 15
    s_result = year % 28
    if s_result == 0:
        s_result = 28
    m_result = year % 19
    if m_result == 0:
        m_result = 19

    if e_result == e and s_result == s and m_result == m:
        break

    year += 1

print(year)