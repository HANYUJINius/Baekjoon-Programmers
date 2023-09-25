total = int(input())
cnt = int(input())
sum = 0

for i in range(cnt):        
    p, c = map(int, input().split())        #p는 price c는 count
    sum += p * c

if sum==total: print("Yes")
else: print("No")