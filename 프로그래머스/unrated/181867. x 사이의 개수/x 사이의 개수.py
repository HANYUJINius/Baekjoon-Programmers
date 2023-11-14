def solution(myString):
    answer = []
    sum = 0
    for i in myString:
        if i == 'x':
            answer.append(sum)
            sum = 0
        else:
            sum += 1
    answer.append(sum)
    return answer