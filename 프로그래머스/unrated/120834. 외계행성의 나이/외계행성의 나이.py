def solution(age):
    answer = ''
    alpha = [chr(word) for word in range(ord('a'), ord('z')+1)]
    for i in str(age):
        answer += alpha[int(i)]
    return answer