medal = int(input("輸入筆數n:"))
dict1 ={}
for i in range(medal):
    a , b = input().split()
    dict1[a]=b
for i,j in dict1.items():
    print(f"{i}牌得到{j}面")