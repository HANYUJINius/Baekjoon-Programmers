def solution(myStr):
    answer = []
    tmp = ''
    for i in myStr:
        if i == 'a' or i == 'b' or i == 'c':
            answer.append(tmp)
            tmp = ''
        else:
            tmp += i
    answer.append(tmp)

    newAnswer = [i for i in answer if i != ""]
    
    if newAnswer == []:
        newAnswer.append("EMPTY")
                
    return newAnswer