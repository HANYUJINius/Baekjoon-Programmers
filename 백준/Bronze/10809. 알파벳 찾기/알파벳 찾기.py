s = input()
alpha = list(chr(i) for i in range(ord('a'), ord('z')+1))
nList = [-1] * len(alpha)

for i in s:
    if i in alpha:
        sIndex = s.index(i)
        alphaIndex = alpha.index(i)
        nList[alphaIndex] = sIndex

for i in nList:
    print(i, end=" ")