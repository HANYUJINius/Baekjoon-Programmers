def solution(n):
    tmp = []
    answer = []
    for i in range(2, n+1):
        if n % i == 0:
            tmp.append(i)
            
    flag = 1    #1은 소수. 일단 소수라고 하자
    for i in tmp:
        for j in range(2, i):
            if i % j == 0:
                flag = 0    #약수가 있으면 소수 아님. 0으로 바꿔주자
        if flag == 1:
            answer.append(i)
        flag = 1
            
    return answer