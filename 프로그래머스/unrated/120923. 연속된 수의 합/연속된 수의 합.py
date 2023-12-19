def solution(num, total):
    answer = []
    ans=0
    cnt=0
    for i in range(1,num):
        cnt+=i

    a =int((total-cnt)/num)

    for i in range(0,num):
        answer.append(a+i)
    return answer