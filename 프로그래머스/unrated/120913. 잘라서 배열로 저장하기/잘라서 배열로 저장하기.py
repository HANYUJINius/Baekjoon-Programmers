def solution(my_str, n):
    answer = []
    tmp = ''
    for i in my_str:
        if len(tmp) < n:
            tmp += i
        elif len(tmp) >= n:
            answer.append(tmp)
            tmp = ''
            tmp += i
    answer.append(tmp)
    return answer