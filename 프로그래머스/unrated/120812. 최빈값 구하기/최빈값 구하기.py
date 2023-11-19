def solution(array):
    answer = 0
    arr = [0] * (max(array)+1)
    for i in array:
        arr[i] +=1
        
    maxIndex = arr.index(max(arr))
    maxNum = max(arr)
    
    cnt = 0
    
    for i in arr:
        if maxNum == i:
            cnt += 1
    if cnt > 1:
        return -1
    return maxIndex
    