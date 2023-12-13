def solution(numbers, k):
    answer = 0
    if(len(numbers)%2 == 0):
        arr = numbers[0::2]
    else:
        arr = numbers * 2
        arr = arr[0::2]
    answer = arr [k % len(arr) - 1]
    return answer