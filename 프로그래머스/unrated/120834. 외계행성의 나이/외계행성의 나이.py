def solution(age):
    answer = ''
    num = [i for i in range(0,27)]
    alpha = [chr(word) for word in range(ord('a'), ord('z')+1)]
    for i in str(age):
        answer += alpha[int(i)]
    return answer