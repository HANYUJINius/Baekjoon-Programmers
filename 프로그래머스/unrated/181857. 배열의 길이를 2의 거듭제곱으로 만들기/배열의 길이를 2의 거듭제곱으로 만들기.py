def solution(arr):
    answer = []
    sq = []
    for i in range(0, 11):
        sq.append(2**i)
    
    arrLen = len(arr)
    
    if arrLen in sq:
        return arr
    
    for i in range(0, len(sq)):
        if arrLen < sq[i]:
            idx = i
            break
    
    again = sq[i] - arrLen
    
    for i in range(0, again):
        arr.append(0)
    
    return arr
    
    