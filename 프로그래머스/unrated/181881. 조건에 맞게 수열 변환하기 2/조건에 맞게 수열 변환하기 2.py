def solution(arr):
    answer = 0
    tmp = []
    copyArr = []
    while(1):
        if copyArr == arr:
            break
        copyArr = arr.copy()
        for i in arr:
            if i >= 50 and i % 2== 0:
                tmp.append(i//2)
            elif i < 50 and i % 2 !=0:
                tmp.append(i*2 + 1)
            else:
                tmp.append(i)
        answer += 1
        arr = tmp.copy()
        tmp = []
    return answer-1