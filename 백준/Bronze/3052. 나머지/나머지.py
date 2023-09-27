arr = []
is_In = []
cnt = 0

for i in range(10):
    num = int(input())
    arr.append(num % 42)
    
for i in arr:
    if i not in is_In:
        is_In.append(i)
        cnt += 1

print(cnt)