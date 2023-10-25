def solution(my_string, alp):
    lst = list(my_string)
    answer = []
    for i in lst:
        if i == alp:
            i = i.upper()
            answer.append(i)
        else:
            answer.append(i)
        ranswer = "".join(answer)
    return ranswer 