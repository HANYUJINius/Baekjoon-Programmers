def solution(quiz):
    answer = []
    for i in quiz:
        res = i.split()
        if(res[1] == '+'):
            sum = int(res[0]) + int(res[2])
        else:
            sum = int(res[0]) - int(res[2])
            
        if(sum == int(res[4])):
            answer.append("O")
        else: answer.append("X")
    return answer