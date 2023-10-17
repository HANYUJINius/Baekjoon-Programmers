def solution(n_str):
    k=0
    for i in range(len(n_str)):
        if(n_str[i] != '0'):
            k = i
            break
    answer = n_str[i:]
    return answer