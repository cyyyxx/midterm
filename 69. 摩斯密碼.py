a = input().split()
for i in a:
    b = i.rstrip("-")
    if len(b)==5:
        c = i.rstrip(".")
        print(5+len(c),end="")
    else:
        print(len(b),end="")