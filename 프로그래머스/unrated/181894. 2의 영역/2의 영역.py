def solution(arr):
    answer = []
    index = []
    
    for i in range(len(arr)):
        if arr[i] == 2:
            index.append(i)
            
    if(len(index)>1):
        for i in range(index[0], index[-1] + 1):
            answer.append(arr[i])
    else:
        answer.append(2)
            
    if len(index)!=0:
        return answer
    return [-1]