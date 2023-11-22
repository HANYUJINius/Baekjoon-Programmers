def solution(array, n):
    answer = 0
    array = sorted(array)
    for i in range(len(array)):
        if n < array[i]:
            break
    if n - array[i-1] > array[i] - n:
        return array[i]
    return array[i-1]
            
