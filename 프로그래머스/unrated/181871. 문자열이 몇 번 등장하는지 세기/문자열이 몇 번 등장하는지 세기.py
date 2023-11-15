def solution(myString, pat):
    answer = 0
    word = ''
    for i in range(len(myString) -len(pat)+1):
        for j in range(len(pat)):
            word += myString[i+j]
        if word == pat:
            answer += 1
        word = ''
    return answer