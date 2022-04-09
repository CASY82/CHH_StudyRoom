import sys
from string import ascii_lowercase

call = "abcabcdefabc"
call = "abxdeydeabz"
call = "ABCabcA"

def countLetters(word):
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter

def solution(call):
    # alpha = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    # alphabet_list = list(ascii_lowercase)

    call_tmp = call.lower()
    # for i in alphabet_list:
    #     alpha[i] += call.count(i)
    #
    # print(call)
    # print(alpha)

    di = countLetters(call_tmp)
    tmp = [k for k,v in di.items() if max(di.values()) == v]

    for i in tmp:
        call = call.replace(i, "")
        call = call.replace(i.upper(), "")

    return call

print(solution(call))