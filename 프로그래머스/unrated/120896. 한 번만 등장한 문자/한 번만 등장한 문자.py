def solution(s):
    answer = ''
    tmp = []
    for i in s:
        k = s.count(i)
        if k == 1:
            answer += i
    new_answer = sorted(answer)
    return ''.join(new_answer)