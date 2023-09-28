word = input()
time = 0

alphaList = ["ABC", "DEF", "GHI", "JKL","MNO","PQRS", "TUV", "WXYZ"]

for alph in alphaList:
    for i in alph:
        for v in word:
            if v==i:
                time += alphaList.index(alph) + 3
print(time)