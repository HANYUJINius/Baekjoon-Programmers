def solution(i, j, k):
    answer = 0
    for i in range(i,j+1):
        for word in str(i):
            if int(word) == k :
                answer+=1
    return answer