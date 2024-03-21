import sys

word = sys.stdin.readline().strip()

if word == "fdsajkl;" or word == "jkl;fdsa":
    print("in-out")
elif word == "asdf;lkj" or word == ";lkjasdf":
    print("out-in")
elif word == "asdfjkl;":
    print("stairs")
elif word == ";lkjfdsa":
    print("reverse")
else:
    print("molu")