have = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]

for i in range(len(have)):
    value = 0
    if chess[i] != have[i]:
        value = chess[i] - have[i]
    print(value, end =" ")
        
        
    

