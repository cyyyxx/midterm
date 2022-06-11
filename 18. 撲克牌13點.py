def poker(x):
    if x=="A":
        return 1
    elif x=="J":
        return 11
    elif x=="Q":
        return 12
    elif x=="K":
        return 13
    else:
        return int(x)
a = input().split()
total = 0
for i in a:
    total+=poker(i)
print(total)