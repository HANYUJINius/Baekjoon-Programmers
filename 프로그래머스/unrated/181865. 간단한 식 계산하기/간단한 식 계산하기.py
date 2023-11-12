def solution(binomial):
    answer = 0
    arr = binomial.split();
    
    arr[0] , arr[2] = int(arr[0]), int(arr[2])
    if arr[1] == '+':
        return arr[0] + arr[2]
    elif arr[1] == '-':
        return arr[0] - arr[2]
    else:
        return arr[0] * arr[2]
