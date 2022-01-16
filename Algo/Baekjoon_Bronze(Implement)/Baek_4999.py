import sys

jaehwan = sys.stdin.readline().strip()
doctor = sys.stdin.readline().strip()

if len(jaehwan) >= len(doctor):
    print("go")
elif len(jaehwan) < len(doctor):
    print("no")