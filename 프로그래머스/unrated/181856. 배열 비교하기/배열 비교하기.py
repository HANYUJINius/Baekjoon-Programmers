def solution(arr1, arr2):
    arr1Sum = 0
    arr2Sum = 0
    if(len(arr1) == len(arr2)):
        for i in arr1:
            arr1Sum+=i
        for i in arr2:
            arr2Sum+=i
        if(arr1Sum == arr2Sum):
            return 0
        return 1 if(arr1Sum > arr2Sum) else -1
    elif (len(arr1) > len(arr2)):
        return 1
    return -1