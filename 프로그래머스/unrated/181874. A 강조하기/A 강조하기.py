def solution(myString):
    answer = ''
    arr = []
    for i in myString:
        if i == 'a' or i =="A":
            arr.append('A')
        else:
            arr.append(i.lower())
    answer = ''.join(arr)
    return answer