def solution(array, commands):
    answer = []
    tmp = []
    for i,j,k in commands:
        tmp = array[i-1:j]
        tmp = sorted(tmp)
        answer.append(tmp[k-1])
        tmp = []
    return answer