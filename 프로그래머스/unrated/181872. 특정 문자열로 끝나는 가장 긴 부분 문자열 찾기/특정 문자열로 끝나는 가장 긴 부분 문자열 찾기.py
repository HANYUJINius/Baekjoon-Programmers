def solution(myString, pat):
    answer = ''
    cnt = myString.count(pat)
    arr = myString.replace(pat, " 0 ").split()
    num = 0
    if cnt > 1:
        for i in arr:
            if num == cnt:
                break
            if i == "0":
                answer += pat
                num += 1
            else:
                answer += i
    else:
        if arr[0] == '0':
            answer += pat
        else:
            answer += arr[0] + pat 
    return answer
    