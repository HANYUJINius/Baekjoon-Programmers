def solution(dots):
    answer = 1
    h = []
    v = []
    for i,j in dots:
        h.append(i)
        v.append(j)
    
    answer = (max(h) - min(h)) * (max(v) - min(v))
    return answer