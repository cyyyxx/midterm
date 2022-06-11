value = input("輸入一字元為:")
list = []
OrList = []
for i in value:
    list.append(i)
    OrList.append(i)
list.reverse()
if list == OrList:
    print("YES")
else:
    print("NO")