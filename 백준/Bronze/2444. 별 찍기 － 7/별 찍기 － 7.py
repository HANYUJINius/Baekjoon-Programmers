star = int(input())

for i in range(1, star+1):
    print(" "*(star-i), end = "")
    print("*"*(2*i-1), end="")
    print("")

for i in range(star-1, 0,-1):
    print(" "*(star-i), end = "")
    print("*"*(2*i-1), end="")
    print("")