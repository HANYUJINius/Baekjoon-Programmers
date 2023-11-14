def solution(my_string):
    answer = [0]*52
    for i in my_string:
        if i.isupper():
            word = ord(i) - 65
            answer[word] += 1
        else:
            word = ord(i) - 71
            answer[word] += 1
            
    return answer