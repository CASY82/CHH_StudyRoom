from collections import Counter

# sentence = "His comments came after Pyongyang announced it had a plan to fire four missiles near the US territory of Guam."
sentence = "Jackdaws love my big sphinx of quartz"

def solution(sentence):
    answer = ""

    sentence = sentence.lower()

    alpha = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',')
    count_alpha = [0 for _ in range(26)]

    for i in range(len(sentence)):
        if sentence[i] in alpha:
            count_alpha[alpha.index(sentence[i])] += 1

    for i in range(26):
        if count_alpha[i] == 0:
            answer += alpha[i]

    if answer == "":
        answer = "perfect"

    return answer

print(solution(sentence))