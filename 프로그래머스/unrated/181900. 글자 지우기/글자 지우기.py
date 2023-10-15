def solution(my_string, indices):
    answer = ''
    word = []
    n_word = []
    for i in my_string:
        word.append(i)
        
    for i in indices:
        word[i] = 0
        
    for i in word:
        if(i != 0):
            n_word.append(i)
        
    answer = "".join(n_word)
    return answer