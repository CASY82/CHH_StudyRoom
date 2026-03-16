# 대전과학고등학교를 아십니까
import sys

while True:
    word = sys.stdin.readline().strip()

    if word == "end":
        break

    if word == "animal":
        print("Panthera tigris")
    elif word == "tree":
        print("Pinus densiflora")
    elif word == "flower":
        print("Forsythia koreana")