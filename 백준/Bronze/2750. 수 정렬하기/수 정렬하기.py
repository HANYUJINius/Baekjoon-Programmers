num = int(input())
num_list = []

for i in range(num):
    num_list.append(int(input()))
    
num_list = sorted(num_list)

for i in num_list:
    print(i)