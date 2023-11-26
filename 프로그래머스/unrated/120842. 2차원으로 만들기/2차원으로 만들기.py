def solution(num_list, n):
    answer = []
    tmp = []
    
    for i in range(0, len(num_list)):
        if i % n != 0 or i == 0:
            tmp.append(num_list[i])
        else:
            answer.append(tmp)
            tmp = []
            tmp.append(num_list[i])
    answer.append(tmp)
    return answer