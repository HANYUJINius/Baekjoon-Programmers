def solution(my_string):
    answer = 0
    sum = 0
    for i in my_string:
        if i.isdigit():
            sum = (sum * 10) + int(i)
        else:
            answer += sum
            sum = 0
    answer += sum
    return answer