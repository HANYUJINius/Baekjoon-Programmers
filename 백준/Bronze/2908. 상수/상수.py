a, b =  input().split()
new_a = 0
new_b = 0

for i in range(len(a)):
    new_a  = new_a * 10 + (int(a) % 10)
    a = int(a) / 10

for i in range(len(b)):
    new_b  = new_b * 10 + (int(b) % 10)
    b = int(b) / 10

print(max(new_a, new_b))