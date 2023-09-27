n,m = map(int, input().split())
basket = [i+1 for i in range(n)]


for cnt in range(m):
    i, j = map(int, input().split())
    reverse = []
    for rev in range(i-1, j):
        reverse.append(basket[rev])
    p =0
    for k in range(i-1, j):
        basket[k] = reverse[len(reverse)-1-p]
        p +=1

for i in range(n):
    print(basket[i], end = " ")