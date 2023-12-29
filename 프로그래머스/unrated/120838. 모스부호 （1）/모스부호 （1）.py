def solution(letter):
    answer = ''
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    } 
    temp = []
    answer = ''
    letter = list(letter.split(" "))

    for key in morse:
        for i in range(len(letter)):
            if letter[i] == key:
                letter[i] = morse[key]
    for i in range(len(letter)):
        answer = answer + letter[i]

    return answer