a = int(input())
space1,space2,star = int(a/2),0,5
for i in range(a):
    if i < int(a/2)+1:
        for j in range(space1):
            print(" ",end="")
        for k in range(0,2*i+1):
            print("*",end="")
        space1 -= 1
        print()
    else:
        space2 += 1
        for j in range(space2):
            print(" ",end="")
        for k in range(0,star):
            print("*",end="")
        star -= 2
        print()