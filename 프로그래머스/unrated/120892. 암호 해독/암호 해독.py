def solution(cipher, code):
    cipher = list(cipher)
    answer = []
    for i in range(0, len(cipher)):
        if (i+1) % code == 0:
            answer.append(cipher[i])
    return ''.join(answer)