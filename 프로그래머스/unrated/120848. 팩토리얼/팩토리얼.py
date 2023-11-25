def solution(n):
    i = 0
    rslt = 1
    while (n>=rslt): 
        i += 1
        rslt*= i
    return i-1
        
        