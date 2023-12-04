def solution(score):
    answer = []
    tmp = []
    
    for i in score:
        tmp.append(sum(i))
        
    sortTmp = sorted(tmp, reverse = True)
    
    for i in tmp:
        answer.append(sortTmp.index(i) + 1)
    return answer