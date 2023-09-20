def is_prime_num(a):
    if a==1:
        return 0
    for i in range(2,a):
        if a % i == 0:
            return 0
    return 1

cnt =0
num = int(input())
arr = list(map(int,input().split()))

for i in arr:
    result = is_prime_num(i)
    if result:
        cnt += 1
print(cnt)
        
    
