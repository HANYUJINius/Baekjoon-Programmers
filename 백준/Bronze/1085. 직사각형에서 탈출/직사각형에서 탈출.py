x,y,w,h = map(int, input().split())
hmin =0
wmin =0

if(h-y < y): hmin = h-y
else: hmin = y
    
if(w - x < x) : wmin = w-x
else: wmin = x

print(min(hmin,wmin))