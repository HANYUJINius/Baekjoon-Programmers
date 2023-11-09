def solution(emergency):
    answer = [0] * len(emergency)
    i = 1
    for i in range(len(emergency)):
        k = emergency.index(max(emergency))
        emergency[k] = -1
        answer[k] = i+1
        i +=1
    return answer