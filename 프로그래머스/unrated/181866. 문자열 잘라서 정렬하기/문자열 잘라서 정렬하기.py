def solution(myString):
    answer = []
    tmp = []
    word = ""
    for i in myString:
        if i == 'x':
            tmp.append(word)
            word = ""
        else:
            word += i
    tmp.append(word)
    for i in tmp:
        if i != "":
            answer.append(i)
    return sorted(answer)